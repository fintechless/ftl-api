src = {
  backend            = "s3"
  config_key_cognito = "terraform/fintechless/ftl-api/aws_cognito_user_pool_client/terraform.tfstate"
  config_key_iam     = "terraform/fintechless/ftl-api/aws_iam_identity_pool/terraform.tfstate"

  description = "IAM role used by the Fintechless Cognito federated identities"
  path        = "/"
}
