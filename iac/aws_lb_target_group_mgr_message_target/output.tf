output "id" {
  value = aws_lb_target_group.this.id
}

output "arn" {
  value = aws_lb_target_group.this.arn
}

output "name" {
  value = aws_lb_target_group.this.name
}

output "port" {
  value = data.terraform_remote_state.aws_k8s_ingress_mgr_message_target.outputs.lb_port
}
