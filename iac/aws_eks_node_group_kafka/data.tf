data "terraform_remote_state" "aws_eks_cluster" {
  backend = var.src.backend
  config  = try(local.config_eks, {})
}

data "terraform_remote_state" "aws_iam_eks_node_group_kafka" {
  backend = var.src.backend
  config  = try(local.config_iam, {})
}
