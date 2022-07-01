src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_transaction/terraform.tfstate"

  mgr            = "transaction"
  container_port = 5016
}
