locals {
  rest_api_id   = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  parent_id     = data.terraform_remote_state.aws_api_gateway_parent_api.outputs.root_resource_id
  authorizer_id = data.terraform_remote_state.aws_api_gateway_authorizer.outputs.id
  connection_id = data.terraform_remote_state.aws_api_gateway_vpc_link.outputs.id
  lb_dns_name   = data.terraform_remote_state.aws_lb.outputs.dns_name
  mgr_port      = data.terraform_remote_state.aws_lb_target_group_mgr_provider_category.outputs.port

  config_api = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_api
  }

  config_parent_api = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_parent_api
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

  config_lb = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_lb
  }

  config_tg = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_tg
  }
}
