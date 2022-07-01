output "ids" {
  value = {
    for k, upc in aws_cognito_user_pool_client.this : k => upc.id
  }
}
