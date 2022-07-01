locals {
  config_cognito = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_cognito
  }

  config_client = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_client
  }

  config_iam = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_iam
  }
}
