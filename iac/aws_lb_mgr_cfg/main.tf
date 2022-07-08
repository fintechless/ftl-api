resource "aws_lb" "this" {
  name               = "${var.src.name}-${local.ftl_env}"
  internal           = var.src.internal
  load_balancer_type = var.src.load_balancer_type
  subnets            = data.terraform_remote_state.aws_eks_cluster.outputs.subnet_ids
}
