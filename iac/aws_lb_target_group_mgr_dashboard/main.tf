resource "aws_lb_target_group" "this" {
  name        = "ftl-mgr-dashboard-tg-${local.ftl_env}"
  target_type = "alb"
  port        = data.terraform_remote_state.aws_k8s_ingress_mgr_dashboard.outputs.lb_port
  protocol    = "TCP"
  vpc_id      = data.terraform_remote_state.aws_eks_cluster.outputs.vpc_id

  health_check {
    enabled = true

    healthy_threshold   = 3
    unhealthy_threshold = 3
    interval            = 30

    path     = data.terraform_remote_state.aws_k8s_ingress_mgr_dashboard.outputs.lb_health_check_path
    port     = "traffic-port"
    protocol = "HTTP"
  }

  tags = var.tags
}

resource "aws_lb_target_group_attachment" "this" {
  target_group_arn = aws_lb_target_group.this.arn
  target_id        = data.aws_lb.this.arn
  port             = data.terraform_remote_state.aws_k8s_ingress_mgr_dashboard.outputs.lb_port
}
