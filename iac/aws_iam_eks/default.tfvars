src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_iam_eks/terraform.tfstate"

  role_name   = "ftl-iam-role-eks-cluster"
  description = "IAM role used by the Fintechless EKS cluster"

  aws_policies = [
    "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
    "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
  ]
}
