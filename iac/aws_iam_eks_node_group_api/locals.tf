locals {
  config = {
    region = local.ftl_active
    bucket = replace(local.ftl_bucket, data.aws_region.this.name, local.ftl_active)
    key    = var.src.config_key
  }
}
