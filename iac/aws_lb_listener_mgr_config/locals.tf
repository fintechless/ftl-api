locals {
  target_groups = {
    config = {
      arn  = data.terraform_remote_state.aws_lb_target_group_mgr_config.outputs.arn
      port = data.terraform_remote_state.aws_lb_target_group_mgr_config.outputs.port
    }
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
