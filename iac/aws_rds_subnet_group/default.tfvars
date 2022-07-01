src = {
  backend               = "s3"
  config_key_eks_cluste = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  name                  = "private-fintechless-aurora"
  description           = "Private Fintechless aurora"
}

tags = {
  Name        = "private-fintechless-aurora"
  Description = "Private Fintechless aurora"
}
