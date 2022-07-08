data "terraform_remote_state" "aws_eks_cluster" {
  backend = var.src.backend
  config  = try(local.config, {})
}
