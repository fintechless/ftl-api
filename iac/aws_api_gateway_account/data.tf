data "terraform_remote_state" "aws_iam_api_gateway" {
  backend = var.src.backend
  config  = try(local.config, {})
}
