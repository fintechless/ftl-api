output "arn" {
  value = {
    for k, v in aws_dynamodb_table.this : k => v.arn
  }
}
