locals {
  config_cognito = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_cognito
  }

  config_iam = {
    region = local.ftl_active
    bucket = replace(local.ftl_bucket, data.aws_region.this.name, local.ftl_active)
    key    = var.src.config_key_iam
  }
}
