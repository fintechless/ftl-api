output "id" {
  value = aws_api_gateway_rest_api.this.id
}

output "root_resource_id" {
  value = aws_api_gateway_rest_api.this.root_resource_id
}

output "body_hash" {
  value = sha1(jsonencode(aws_api_gateway_rest_api.this.body))
}
