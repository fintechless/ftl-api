src = {
  backend            = "s3"
  config_key_cognito = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"
  config_key_lambda  = "terraform/fintechless/ftl-api/aws_lambda_user_pool/terraform.tfstate"

  statement_id = "AllowExecutionFromCognito"
  action       = "lambda:InvokeFunction"
  principal    = "cognito-idp.amazonaws.com"
}
