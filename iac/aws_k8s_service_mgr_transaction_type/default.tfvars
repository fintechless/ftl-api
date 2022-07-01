src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_transaction_type/terraform.tfstate"

  mgr            = "transaction-type"
  container_port = 5014
}
