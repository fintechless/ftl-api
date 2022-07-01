src = {
  backend            = "s3"
  config_key_cognito = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"
  config_key_iam     = "terraform/fintechless/ftl-api/aws_iam_lambda_user_pool/terraform.tfstate"

  role_name   = "ftl-api-lambda-user-pool-role"
  policy_name = "ftl-api-lambda-user-pool-policy"
  description = "IAM role used by the Fintechless Lambda function"
  path        = "/"
}
