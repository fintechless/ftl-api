src = {
  backend        = "s3"
  config_key_eks = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  config_key_iam = "terraform/fintechless/ftl-api/aws_iam_eks_node_group_api/terraform.tfstate"

  node_group_name = "ftl-api-msa-node-group"
  instance_types  = ["t3.micro"]
  ami_type        = "AL2_x86_64"

  scaling_config = {
    desired_size = 10
    max_size     = 10
    min_size     = 10
  }
}
