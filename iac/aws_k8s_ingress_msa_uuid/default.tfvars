src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_k8s_deployment_msa_uuid/terraform.tfstate"

  msa            = "uuid"
  image_version  = "latest"
  container_port = 5002
}
