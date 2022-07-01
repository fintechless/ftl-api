src = {
  backend       = "s3"
  config_key_lb = "terraform/fintechless/ftl-api/aws_lb_msa/terraform.tfstate"
  config_key_tg = "terraform/fintechless/ftl-api/aws_lb_target_group_msa_ping/terraform.tfstate"

  port     = "443"
  protocol = "TCP"
}
