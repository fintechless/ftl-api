src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_msa_ping/terraform.tfstate"

  msa            = "ping"
  image_version  = "latest"
  container_port = 5000
}
