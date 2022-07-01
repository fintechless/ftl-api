resource "aws_cognito_resource_server" "this" {
  identifier   = var.src.identifier
  name         = var.src.name
  user_pool_id = data.terraform_remote_state.aws_cognito_user_pool.outputs.id

  dynamic "scope" {
    for_each = var.scopes
    content {
      scope_name        = scope.value.name
      scope_description = scope.value.description
    }
  }
}
