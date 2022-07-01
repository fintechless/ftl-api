src = {
  backend        = "s3"
  config_key_eks = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  config_key_iam = "terraform/fintechless/ftl-api/aws_iam_eks_node_group_kafka/terraform.tfstate"

  node_group_name = "ftl-api-kafka-node-group"
  instance_types  = ["t3.small"]
  ami_type        = "AL2_x86_64"

  scaling_config = {
    desired_size = 3
    max_size     = 25
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
