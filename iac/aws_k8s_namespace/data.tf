data "terraform_remote_state" "aws_iam_eks_node_group_api" {
  backend = var.src.backend
  config  = try(local.config_api, {})
}

data "terraform_remote_state" "aws_iam_eks_node_group_default" {
  backend = var.src.backend
  config  = try(local.config_default, {})
}

data "terraform_remote_state" "aws_iam_eks_node_group_kafka" {
  backend = var.src.backend
  config  = try(local.config_kafka, {})
}

data "aws_iam_roles" "this" {
  name_regex = ".*node-group-iam-role.*"
}
