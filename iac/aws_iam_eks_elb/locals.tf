locals {
  oidc_issuer_sub = replace("${data.terraform_remote_state.aws_eks_cluster.outputs.oidc_issuer}:sub", "https://", "")
  oidc_issuer_aud = replace("${data.terraform_remote_state.aws_eks_cluster.outputs.oidc_issuer}:aud", "https://", "")

  config_eks = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_eks
  }

  config_iam = {
    region = local.ftl_active
    bucket = replace(local.ftl_bucket, data.aws_region.this.name, local.ftl_active)
    key    = var.src.config_key_iam
  }
}
