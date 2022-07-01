src = {
  backend        = "s3"
  config_key_iam = "terraform/fintechless/ftl-api/aws_iam_eks/terraform.tfstate"
  config_key_sgr = "terraform/fintechless/ftl-api/aws_sg_eks/terraform.tfstate"

  cluster_name  = "ftl-api-k8s"
  alb_name      = "ftl-msa-lb"
  k8s_namespace = "fintechless"
  k8s_version   = "0.0.1"
  k8s_port      = 5000
}
