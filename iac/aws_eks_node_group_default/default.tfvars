src = {
  backend        = "s3"
  config_key_eks = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  config_key_iam = "terraform/fintechless/ftl-api/aws_iam_eks_node_group_default/terraform.tfstate"

  node_group_name = "ftl-api-default-node-group"
  ami_type        = "AL2_x86_64"
  capacity_type   = "SPOT"
  instance_types  = ["t3.small"]

  scaling_config = {
    desired_size = 1
    max_size     = 1
    min_size     = 1
  }

  aws_policies = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
    "arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy",
    "arn:aws:iam::aws:policy/AmazonDynamoDBFullAccess",
    "arn:aws:iam::aws:policy/AmazonS3FullAccess",
  ]
}
