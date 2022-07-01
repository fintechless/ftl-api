output "ids" {
  value = { for k, cip in aws_cognito_identity_pool.this : k => cip.id }
}

output "arns" {
  value = { for k, cip in aws_cognito_identity_pool.this : k => cip.arn }
}
