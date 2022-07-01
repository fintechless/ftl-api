data "terraform_remote_state" "aws_cognito_user_pool" {
  backend = var.src.backend
  config  = try(local.config_cognito, {})
}

data "terraform_remote_state" "aws_cognito_user_group" {
  backend = var.src.backend
  config  = try(local.config_user_group, {})
}

data "terraform_remote_state" "aws_cognito_resource_server" {
  backend = var.src.backend
  config  = try(local.config_resource, {})
}
