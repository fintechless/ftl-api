locals {
  config_eks_cluste = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_eks_cluste
  }
}
