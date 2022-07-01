src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_dashboard/terraform.tfstate"

  mgr            = "dashboard"
  container_port = 5028
}
