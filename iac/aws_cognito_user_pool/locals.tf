locals {
  config = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key
  }

  email_configuration_source = var.src.email_configuration.name == null ? null : format("arn:aws:ses:%s:%s:identity/%s", local.ftl_active, data.aws_caller_identity.this.account_id, var.src.email_configuration.name)
}
