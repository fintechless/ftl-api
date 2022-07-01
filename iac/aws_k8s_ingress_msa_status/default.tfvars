src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_msa_status/terraform.tfstate"

  msa            = "status"
  image_version  = "latest"
  container_port = 5006
}
