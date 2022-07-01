resource "aws_api_gateway_authorizer" "this" {
  name            = "${var.src.name}-${local.ftl_env}"
  type            = var.src.type
  identity_source = var.src.identity_source
  rest_api_id     = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  provider_arns   = [data.terraform_remote_state.aws_cognito_user_pool.outputs.arn]
}
