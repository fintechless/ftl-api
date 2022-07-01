resource "aws_cognito_user_pool_client" "this" {
  for_each = { for ug in data.terraform_remote_state.aws_cognito_user_group.outputs.user_groups : ug.name => ug }

  name          = "${each.value.name}-${local.ftl_env}"
  callback_urls = [format("https://%s/%s", local.ftl_fqdn_app, try(each.value.default_redirect_uri, ""))]
  user_pool_id  = data.terraform_remote_state.aws_cognito_user_pool.outputs.id

  allowed_oauth_flows_user_pool_client = tobool(var.src.allowed_oauth_flows_user_pool_client)
  explicit_auth_flows                  = try(each.value.explicit_auth_flows, [])
  allowed_oauth_flows                  = try(each.value.allowed_oauth_flows, "")
  allowed_oauth_scopes                 = setunion(each.value.allowed_oauth_scopes, data.terraform_remote_state.aws_cognito_resource_server.outputs.scope_identifiers)
  access_token_validity                = try(each.value.access_valid, "")
  id_token_validity                    = try(each.value.id_token_validity, "")
  refresh_token_validity               = try(each.value.refresh_valid, "")
  generate_secret                      = try(each.value.generate_secret, "")
  supported_identity_providers         = var.src.supported_identity_providers
  read_attributes                      = try(each.value.read_attributes, [])
  write_attributes                     = try(each.value.write_attributes, [])

  token_validity_units {
    id_token      = try(each.value.id_token, "")
    access_token  = try(each.value.access_token, "")
    refresh_token = try(each.value.refresh_token, "")
  }
}

resource "aws_secretsmanager_secret" "this" {
  for_each = { for upc in aws_cognito_user_pool_client.this : upc.name => upc }
  name     = format("%s-%s", each.value.name, data.aws_region.this.name)
}

resource "aws_secretsmanager_secret_version" "this" {
  for_each  = { for upc in aws_cognito_user_pool_client.this : upc.name => upc }
  secret_id = aws_secretsmanager_secret.this[each.value.name].id
  secret_string = jsonencode({
    client_is     = each.value.id
    client_secret = each.value.client_secret
    user_pool_id  = each.value.user_pool_id
  })
}
