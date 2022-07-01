src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_message_definition/terraform.tfstate"

  mgr            = "message-definition"
  image_version  = "latest"
  container_port = 5024
}
