src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_microservice/terraform.tfstate"

  mgr            = "microservice"
  image_version  = "latest"
  container_port = 5008
}
