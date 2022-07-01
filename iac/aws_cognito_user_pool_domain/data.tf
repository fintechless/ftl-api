data "aws_acm_certificate" "this" {
  count  = local.ftl_domain == "" ? 0 : 1
  domain = local.ftl_domain
}

data "terraform_remote_state" "aws_cognito_user_pool" {
  backend = var.src.backend
  config  = try(local.config, {})
}
