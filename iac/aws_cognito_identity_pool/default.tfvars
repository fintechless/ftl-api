src = {
  backend            = "s3"
  config_key_cognito = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"
  config_key_client  = "terraform/fintechless/ftl-api/aws_cognito_user_pool_client/terraform.tfstate"
  config_key_iam     = "terraform/fintechless/ftl-api/aws_iam_identity_pool/terraform.tfstate"

  allow_unauthenticated_identities = false
  allow_classic_flow               = false
}
