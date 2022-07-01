resource "aws_api_gateway_domain_name" "this" {
  count                    = local.ftl_domain == "" ? 0 : 1
  domain_name              = local.ftl_fqdn_api
  regional_certificate_arn = data.aws_acm_certificate.this[0].arn
  security_policy          = var.src.security_policy

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_base_path_mapping" "this" {
  count       = local.ftl_domain == "" ? 0 : 1
  api_id      = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  stage_name  = data.terraform_remote_state.aws_api_gateway_deployment.outputs.stage_name
  domain_name = local.ftl_fqdn_api
}
