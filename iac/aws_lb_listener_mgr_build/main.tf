resource "aws_lb_listener" "this" {
  for_each          = local.target_groups
  load_balancer_arn = data.terraform_remote_state.aws_lb.outputs.arn
  protocol          = var.src.protocol
  port              = each.value.port

  default_action {
    type             = "forward"
    target_group_arn = each.value.arn
  }
}
