src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_message_target/terraform.tfstate"

  mgr            = "message-target"
  image_version  = "latest"
  container_port = 5026
}
