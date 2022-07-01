src = {
  backend        = "s3"
  config_key_eks = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  config_key_iam = "terraform/fintechless/ftl-api/aws_iam_eks_elb/terraform.tfstate"

  role_name   = "ftl-iam-role-eks-elb-controller"
  policy_name = "ftl-iam-policy-eks-elb-controller"
  description = "IAM role and policy used by the Fintechless EKS cluster"
  path        = "/"
}
