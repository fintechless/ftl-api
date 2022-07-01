data "terraform_remote_state" "aws_api_gateway_rest_api" {
  backend = var.src.backend
  config  = try(local.config, {})
}
