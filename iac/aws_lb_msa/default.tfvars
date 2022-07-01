src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"

  name               = "ftl-api-lb"
  internal           = "true"
  load_balancer_type = "network"
}
