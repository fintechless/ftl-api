data "terraform_remote_state" "aws_eks_cluste" {
  backend = var.src.backend
  config  = try(local.config_eks_cluste, {})
}

data "aws_subnet" "this" {
  for_each = toset(data.terraform_remote_state.aws_eks_cluste.outputs.subnet_ids)
  id       = each.value
}
