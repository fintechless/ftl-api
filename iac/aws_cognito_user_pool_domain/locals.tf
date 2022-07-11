locals {
  config = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key
  }

  custom_domain  = format("%s.%s", local.ftl_env == "default" ? local.ftl_subdomain_auth : "${local.ftl_subdomain_auth}-${local.ftl_env}", local.ftl_domain)
  default_domain = format("%s-%s", local.ftl_env == "default" ? local.ftl_subdomain_auth : "${local.ftl_subdomain_auth}-${local.ftl_env}", "fintechless")
}
