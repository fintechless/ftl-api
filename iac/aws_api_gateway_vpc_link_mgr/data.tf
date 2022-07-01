data "terraform_remote_state" "aws_lb" {
  backend = var.src.backend
  config  = try(local.config, {})
}
