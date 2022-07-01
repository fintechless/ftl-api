data "terraform_remote_state" "user_pool_client" {
  backend = var.src.backend
  config  = try(local.config_cognito, {})
}

data "terraform_remote_state" "aws_iam_identity_pool" {
  count   = (data.aws_region.this.name == local.ftl_passive) ? 1 : 0
  backend = var.src.backend
  config  = try(local.config_iam, {})
}
