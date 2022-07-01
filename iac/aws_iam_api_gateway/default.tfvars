src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_iam_api_gateway/terraform.tfstate"

  role_name   = "ftl-api-gateway-cloudwatch-role"
  policy_name = "ftl-api-gateway-cloudwatch-policy"
}
