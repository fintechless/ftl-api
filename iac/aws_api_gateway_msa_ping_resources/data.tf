data "terraform_remote_state" "aws_api_gateway_rest_api" {
  backend = var.src.backend
  config  = try(local.config_api, {})
}

data "terraform_remote_state" "aws_api_gateway_authorizer" {
  backend = var.src.backend
  config  = try(local.config_auth, {})
}

data "terraform_remote_state" "aws_api_gateway_vpc_link" {
  backend = var.src.backend
  config  = try(local.config_link, {})
}

data "terraform_remote_state" "aws_api_gateway_msa_ping" {
  backend = var.src.backend
  config  = try(local.config_msa, {})
}
