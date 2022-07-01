src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_iam_eks_node_group_api/terraform.tfstate"

  role_name   = "ftl-api-msa-node-group-iam-role"
  description = "IAM role used by the Fintechless EKS cluster"

  aws_policies = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
    "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy",
    "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
    "arn:aws:iam::aws:policy/AmazonS3FullAccess",
    "arn:aws:iam::aws:policy/SecretsManagerReadWrite"
  ]
}
