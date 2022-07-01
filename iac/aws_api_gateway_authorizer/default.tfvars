src = {
  backend            = "s3"
  config_key_api     = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"
  config_key_cognito = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"

  name            = "ftl-api-gateway-authorizer"
  type            = "COGNITO_USER_POOLS"
  identity_source = "method.request.header.Authorization"
}
