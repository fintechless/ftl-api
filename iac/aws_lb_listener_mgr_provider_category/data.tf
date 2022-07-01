data "terraform_remote_state" "aws_lb" {
  backend = var.src.backend
  config  = try(local.config_lb, {})
}

data "terraform_remote_state" "aws_lb_target_group_mgr_provider_category" {
  backend = var.src.backend
  config  = try(local.config_tg, {})
}
