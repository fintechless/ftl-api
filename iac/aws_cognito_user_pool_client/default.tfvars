src = {
  backend               = "s3"
  config_key_cognito    = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"
  config_key_user_group = "terraform/fintechless/ftl-api/aws_cognito_user_group/terraform.tfstate"
  config_key_resource   = "terraform/fintechless/ftl-api/aws_cognito_resource_server/terraform.tfstate"

  prevent_user_existence_errors        = "ENABLED"
  allowed_oauth_flows_user_pool_client = "true"
  supported_identity_providers         = ["COGNITO"]
}
