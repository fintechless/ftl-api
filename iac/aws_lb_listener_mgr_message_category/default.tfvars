src = {
  backend       = "s3"
  config_key_lb = "terraform/fintechless/ftl-api/aws_lb_mgr/terraform.tfstate"
  config_key_tg = "terraform/fintechless/ftl-api/aws_lb_target_group_mgr_message_category/terraform.tfstate"

  port     = "443"
  protocol = "TCP"
}
