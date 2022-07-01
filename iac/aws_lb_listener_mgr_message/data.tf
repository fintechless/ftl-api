data "terraform_remote_state" "aws_lb" {
  backend = var.src.backend
  config  = try(local.config_lb, {})
}

data "terraform_remote_state" "aws_lb_target_group_mgr_message" {
  backend = var.src.backend
  config  = try(local.config_tg, {})
}
