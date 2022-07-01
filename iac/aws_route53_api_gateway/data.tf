data "aws_route53_zone" "this" {
  count = local.ftl_domain == "" ? 0 : 1
  name  = local.ftl_domain
}

data "terraform_remote_state" "aws_api_gateway_domain_name" {
  backend = var.src.backend
  config  = try(local.config, {})
}
