resource "aws_db_subnet_group" "this" {
  name        = var.src.name
  description = var.src.description
  subnet_ids  = data.terraform_remote_state.aws_eks_cluste.outputs.subnet_ids

  tags = var.tags
}
