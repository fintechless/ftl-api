output "arns" {
  value = try({ for k, r in aws_iam_role.this : k => r.arn }, try(data.terraform_remote_state.aws_iam_identity_pool[0].outputs.arns, {}))
}

output "names" {
  value = try({ for k, r in aws_iam_role.this : k => r.name }, try(data.terraform_remote_state.aws_iam_identity_pool[0].outputs.names, {}))
}
