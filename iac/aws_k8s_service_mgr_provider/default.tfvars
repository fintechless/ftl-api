src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_provider/terraform.tfstate"

  mgr            = "provider"
  container_port = 5030
}
