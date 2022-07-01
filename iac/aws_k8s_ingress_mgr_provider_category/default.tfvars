src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_mgr_provider_category/terraform.tfstate"

  mgr            = "provider-category"
  image_version  = "latest"
  container_port = 5032
}
