src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"

  description       = "API Gateway Deployment for Fintechless REST API"
  stage_description = "API Gateway Stage for Fintechless REST API"
  stage_name        = "v1"
  retention_in_days = "14"
  name_prefix       = "API-Gateway-Execution-Logs"
}
