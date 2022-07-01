resource "aws_eks_node_group" "this" {
  cluster_name    = local.cluster_name
  node_group_name = local.node_group_name
  node_role_arn   = local.role_arn

  subnet_ids = local.subnet_ids

  scaling_config {
    desired_size = var.src.scaling_config.desired_size
    max_size     = var.src.scaling_config.max_size
    min_size     = var.src.scaling_config.min_size
  }

  ami_type       = var.src.ami_type
  instance_types = toset(var.src.instance_types)
  capacity_type  = "SPOT"

  taint {
    key    = "reserved-pool"
    value  = "true"
    effect = "NO_SCHEDULE"
  }

  tags = {
    Name = local.node_group_name
  }
}
