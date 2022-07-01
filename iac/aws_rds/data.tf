data "terraform_remote_state" "aws_rds_subnet_group" {
  backend = var.src.backend
  config  = try(local.config_rds_subnet_group, {})
}

data "terraform_remote_state" "aws_eks_cluster" {
  backend = var.src.backend
  config  = try(local.config_eks_cluster, {})
}
