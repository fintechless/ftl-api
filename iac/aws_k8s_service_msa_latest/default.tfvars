src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_msa_latest/terraform.tfstate"

  msa            = "latest"
  container_port = 5004
}
