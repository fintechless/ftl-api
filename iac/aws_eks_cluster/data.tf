data "aws_subnets" "this" {
  filter {
    name   = "tag:Name"
    values = ["shared-private-*"]
  }

  filter {
    name   = "vpc-id"
    values = [data.terraform_remote_state.aws_sg_eks.outputs.vpc_id]
  }
}

data "terraform_remote_state" "aws_iam_eks" {
  backend = var.src.backend
  config  = try(local.config_iam, {})
}

data "terraform_remote_state" "aws_sg_eks" {
  backend = var.src.backend
  config  = try(local.config_sgr, {})
}
