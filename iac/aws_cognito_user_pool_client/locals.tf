locals {
  config_cognito = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_cognito
  }

  config_user_group = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_user_group
  }

  config_resource = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_resource
  }
}
