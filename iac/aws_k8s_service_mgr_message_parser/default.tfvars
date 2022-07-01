src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_message_parser/terraform.tfstate"

  mgr            = "message-parser"
  container_port = 5040
}
