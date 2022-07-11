resource "aws_cognito_user_pool_domain" "this" {
  domain          = local.ftl_domain == "" ? local.default_domain : local.custom_domain
  certificate_arn = local.ftl_domain == "" ? null : data.aws_acm_certificate.this[0].arn
  user_pool_id    = data.terraform_remote_state.aws_cognito_user_pool.outputs.id
}

resource "aws_secretsmanager_secret_version" "this" {
  count      = local.ftl_domain == "" ? 1 : 0
  depends_on = [aws_cognito_user_pool_domain.this]
  secret_id  = data.aws_secretsmanager_secret.this.id
  secret_string = jsonencode(merge(local.ftl_cicd_secret_map, {
    FTL_FQDN_AUTH = aws_cognito_user_pool_domain.this.domain
  }))
}
