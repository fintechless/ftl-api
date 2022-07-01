data "aws_lb" "this" {
  tags = {
    "elbv2.k8s.aws/cluster" = data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name
    "ingress.k8s.aws/stack" = data.terraform_remote_state.aws_eks_cluster.outputs.alb_name
  }
}

data "terraform_remote_state" "aws_eks_cluster" {
  backend = var.src.backend
  config  = try(local.config_eks, {})
}

data "terraform_remote_state" "aws_k8s_ingress_mgr_provider" {
  backend = var.src.backend
  config  = try(local.config_k8s, {})
}
