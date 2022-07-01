data "terraform_remote_state" "aws_iam_eks_node_group_kafka" {
  count   = (data.aws_region.this.name == local.ftl_passive) ? 1 : 0
  backend = var.src.backend
  config  = try(local.config, {})
}
