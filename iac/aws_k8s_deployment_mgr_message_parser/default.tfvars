src = {
  backend         = "s3"
  config_key_ecr  = "terraform/fintechless/ftl-api/aws_ecr_repository/terraform.tfstate"
  config_key_node = "terraform/fintechless/ftl-api/aws_eks_node_group_api/terraform.tfstate"

  mgr           = "message-parser"
  replicas      = 1
  image_version = "latest"
}
