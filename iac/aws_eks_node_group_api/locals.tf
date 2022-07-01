locals {
  node_group_name = "${var.src.node_group_name}-${local.ftl_env}"
  cluster_name    = data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name
  subnet_ids      = data.terraform_remote_state.aws_eks_cluster.outputs.subnet_ids
  role_arn        = data.terraform_remote_state.aws_iam_eks_node_group_api.outputs.arn

  config_eks = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_eks
  }

  config_iam = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_iam
  }
}
