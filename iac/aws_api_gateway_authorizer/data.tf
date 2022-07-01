data "terraform_remote_state" "aws_api_gateway_rest_api" {
  backend = var.src.backend
  config  = try(local.config_api, {})
}

data "terraform_remote_state" "aws_cognito_user_pool" {
  backend = var.src.backend
  config  = try(local.config_cognito, {})
}
