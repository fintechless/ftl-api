data "tls_certificate" "this" {
  url = data.terraform_remote_state.aws_eks_cluster.outputs.oidc_issuer
}

data "terraform_remote_state" "aws_eks_cluster" {
  backend = var.src.backend
  config  = try(local.config_eks, {})
}

data "terraform_remote_state" "aws_iam_eks_elb" {
  count   = (data.aws_region.this.name == local.ftl_passive) ? 1 : 0
  backend = var.src.backend
  config  = try(local.config_iam, {})
}
