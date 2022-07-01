locals {
  config_eks = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_eks
  }

  config_k8s = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_k8s
  }
}
