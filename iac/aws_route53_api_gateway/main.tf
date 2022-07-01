resource "aws_route53_record" "this" {
  count   = local.ftl_domain == "" ? 0 : 1
  name    = local.ftl_fqdn_api
  type    = var.src.record_type
  zone_id = data.aws_route53_zone.this[0].zone_id

  alias {
    evaluate_target_health = true
    name                   = data.terraform_remote_state.aws_api_gateway_domain_name.outputs.regional_domain_name
    zone_id                = data.terraform_remote_state.aws_api_gateway_domain_name.outputs.regional_zone_id
  }
}
