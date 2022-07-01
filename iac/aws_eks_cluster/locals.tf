locals {
  cluster_name = "${var.src.cluster_name}-${local.ftl_env}"
  alb_name     = "${var.src.alb_name}-${local.ftl_env}"

  config_iam = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_iam
  }

  config_sgr = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_sgr
  }
}
