data "terraform_remote_state" "aws_iam_lambda_user_pool" {
  backend = var.src.backend
  config  = try(local.config, {})
}
