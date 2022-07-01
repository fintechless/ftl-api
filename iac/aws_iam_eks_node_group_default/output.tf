output "arn" {
  value = try(aws_iam_role.this[0].arn, try(data.terraform_remote_state.aws_iam_eks_node_group_default[0].outputs.arn, ""))
}

output "name" {
  value = try(aws_iam_role.this[0].name, try(data.terraform_remote_state.aws_iam_eks_node_group_default[0].outputs.name, ""))
}
