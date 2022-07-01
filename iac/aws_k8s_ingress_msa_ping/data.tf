data "terraform_remote_state" "aws_k8s_deployment_msa_ping" {
  backend = var.src.backend
  config  = try(local.config, {})
}
