src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_provider_subcategory/terraform.tfstate"

  mgr            = "provider-subcategory"
  image_version  = "latest"
  container_port = 5034
}
