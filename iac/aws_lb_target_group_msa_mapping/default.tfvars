src = {
  backend        = "s3"
  config_key_eks = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  config_key_k8s = "terraform/fintechless/ftl-api/aws_k8s_ingress_msa_mapping/terraform.tfstate"
}

tags = {
  Description = "AWS LB Target Group for MSA MAPPING -- Used by the VPC Link NLB"
}
