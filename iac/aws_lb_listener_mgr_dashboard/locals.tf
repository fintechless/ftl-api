locals {
  target_groups = {
    dashboard = {
      arn  = data.terraform_remote_state.aws_lb_target_group_mgr_dashboard.outputs.arn
      port = data.terraform_remote_state.aws_lb_target_group_mgr_dashboard.outputs.port
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
