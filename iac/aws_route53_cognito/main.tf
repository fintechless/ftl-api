resource "aws_route53_record" "this" {
  count   = local.ftl_domain == "" ? 0 : 1
  name    = data.terraform_remote_state.aws_cognito_user_pool_domain.outputs.domain
  type    = var.src.record_type
  zone_id = data.aws_route53_zone.this[0].zone_id

  alias {
    evaluate_target_health = true
    name                   = data.terraform_remote_state.aws_cognito_user_pool_domain.outputs.cloudfront_distribution_arn
    zone_id                = var.src.zone_id
  }
}

resource "aws_secretsmanager_secret_version" "this" {
  depends_on = [aws_route53_record.this]
  secret_id  = data.aws_secretsmanager_secret.this.id
  secret_string = jsonencode(merge(local.ftl_cicd_secret_map, {
    FTL_FQDN_AUTH = data.terraform_remote_state.aws_cognito_user_pool_domain.outputs.domain
  }))
}
