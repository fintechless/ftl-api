data "terraform_remote_state" "aws_ecr_repository" {
  backend = var.src.backend
  config  = try(local.config_ecr, {})
}

data "terraform_remote_state" "aws_eks_node_group_api" {
  backend = var.src.backend
  config  = try(local.config_node, {})
}
