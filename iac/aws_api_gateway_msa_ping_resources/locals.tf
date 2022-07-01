locals {
  rest_api_id   = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  parent_id     = data.terraform_remote_state.aws_api_gateway_msa_ping.outputs.id
  authorizer_id = data.terraform_remote_state.aws_api_gateway_authorizer.outputs.id
  connection_id = data.terraform_remote_state.aws_api_gateway_vpc_link.outputs.id

  config_api = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_api
  }

  config_auth = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_auth
  }

  config_link = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_link
  }

  config_msa = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_msa
  }
}
