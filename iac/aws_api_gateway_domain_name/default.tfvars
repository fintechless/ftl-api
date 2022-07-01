src = {
  backend           = "s3"
  config_key_api    = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"
  config_key_deploy = "terraform/fintechless/ftl-api/aws_api_gateway_deployment/terraform.tfstate"

  security_policy = "TLS_1_2"
}
