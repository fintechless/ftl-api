data "terraform_remote_state" "aws_cognito_user_pool" {
  backend = var.src.backend
  config  = try(local.config_cognito, {})
}

data "terraform_remote_state" "aws_cognito_user_pool_client" {
  backend = var.src.backend
  config  = try(local.config_client, {})
}

data "terraform_remote_state" "aws_iam_identity_pool" {
  backend = var.src.backend
  config  = try(local.config_iam, {})
}
