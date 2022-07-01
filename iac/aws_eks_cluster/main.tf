resource "aws_eks_cluster" "this" {
  name     = local.cluster_name
  role_arn = data.terraform_remote_state.aws_iam_eks.outputs.arn

  vpc_config {
    subnet_ids         = data.aws_subnets.this.ids
    security_group_ids = [data.terraform_remote_state.aws_sg_eks.outputs.id]
  }

  version = "1.22"

  tags = {
    Name = local.cluster_name
  }

  lifecycle {
    prevent_destroy = true
  }
}
