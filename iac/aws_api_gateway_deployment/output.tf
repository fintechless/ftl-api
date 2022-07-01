output "id" {
  value = aws_api_gateway_deployment.this.id
}

output "stage_name" {
  value = aws_api_gateway_stage.this.stage_name
}
