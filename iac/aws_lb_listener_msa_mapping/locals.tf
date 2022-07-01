locals {
  target_groups = {
    mapping = {
      arn  = data.terraform_remote_state.aws_lb_target_group_msa_mapping.outputs.arn
      port = data.terraform_remote_state.aws_lb_target_group_msa_mapping.outputs.port
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
