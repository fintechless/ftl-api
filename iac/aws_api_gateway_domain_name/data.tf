data "aws_acm_certificate" "this" {
  count  = local.ftl_domain == "" ? 0 : 1
  domain = local.ftl_domain
}

data "aws_route53_zone" "this" {
  count = local.ftl_domain == "" ? 0 : 1
  name  = local.ftl_domain
}

data "terraform_remote_state" "aws_api_gateway_deployment" {
  backend = var.src.backend
  config  = try(local.config_deploy, {})
}

data "terraform_remote_state" "aws_api_gateway_rest_api" {
  backend = var.src.backend
  config  = try(local.config_api, {})
}
