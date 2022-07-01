output "arn" {
  value = try(aws_iam_role.this[0].arn, try(data.terraform_remote_state.aws_iam_lambda_user_pool[0].outputs.arn, ""))
}

output "name" {
  value = try(aws_iam_role.this[0].name, try(data.terraform_remote_state.aws_iam_lambda_user_pool[0].outputs.name, ""))
}
