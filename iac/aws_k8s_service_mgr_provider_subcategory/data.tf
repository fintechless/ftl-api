data "terraform_remote_state" "aws_k8s_deployment_mgr_provider_subcategory" {
  backend = var.src.backend
  config  = try(local.config, {})
}
