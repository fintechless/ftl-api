data "terraform_remote_state" "aws_k8s_deployment_mgr_message" {
  backend = var.src.backend
  config  = try(local.config, {})
}
