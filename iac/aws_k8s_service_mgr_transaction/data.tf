data "terraform_remote_state" "aws_k8s_deployment_mgr_transaction" {
  backend = var.src.backend
  config  = try(local.config, {})
}
