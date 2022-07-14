src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_build/terraform.tfstate"

  mgr            = "build"
  container_port = 5042
}
