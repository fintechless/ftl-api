data "terraform_remote_state" "aws_lb" {
  backend = var.src.backend
  config  = try(local.config_lb, {})
}

data "terraform_remote_state" "aws_lb_target_group_msa_uuid" {
  backend = var.src.backend
  config  = try(local.config_tg, {})
}
