locals {
  config_rds_subnet_group = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_rds_subnet_group
  }

  config_eks_cluster = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_eks_cluster
  }
}
