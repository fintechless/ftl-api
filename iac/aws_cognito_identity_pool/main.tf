resource "aws_cognito_identity_pool" "this" {
  for_each                         = data.terraform_remote_state.aws_cognito_user_pool_client.outputs.ids
  identity_pool_name               = "${each.key}-cognito-identity-pool-${local.ftl_env}"
  allow_unauthenticated_identities = tobool(var.src.allow_unauthenticated_identities)
  allow_classic_flow               = tobool(var.src.allow_unauthenticated_identities)

  cognito_identity_providers {
    client_id               = each.value
    provider_name           = data.terraform_remote_state.aws_cognito_user_pool.outputs.endpoint
    server_side_token_check = false
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_cognito_identity_pool_roles_attachment" "this" {
  for_each         = { for k, cip in aws_cognito_identity_pool.this : k => cip.id }
  identity_pool_id = each.value

  roles = {
    authenticated = data.terraform_remote_state.aws_iam_identity_pool.outputs.arns[each.key]
  }
}
