data "terraform_remote_state" "aws_cognito_user_pool" {
  backend = var.src.backend
  config  = try(local.config_cognito, {})
}

data "terraform_remote_state" "aws_iam_lambda_user_pool" {
  backend = var.src.backend
  config  = try(local.config_iam, {})
}

