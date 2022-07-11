data "aws_subnet" "this" {
  for_each = toset(split(",", local.ftl_active_subnets))
  id       = each.value
}

data "terraform_remote_state" "aws_iam_eks" {
  backend = var.src.backend
  config  = try(local.config_iam, {})
}

data "terraform_remote_state" "aws_sg_eks" {
  backend = var.src.backend
  config  = try(local.config_sgr, {})
}
