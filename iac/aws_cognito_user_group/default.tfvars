src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"

  user_groups = [
    {
      name                 = "ftl-group-web-admin"
      description          = "Cognito User Groups for FTL Web Admin"
      allowed_oauth_flows  = ["code", "implicit"]
      allowed_oauth_scopes = ["phone", "email", "openid", "profile", "aws.cognito.signin.user.admin"]
      explicit_auth_flows  = ["ALLOW_USER_PASSWORD_AUTH", "ALLOW_CUSTOM_AUTH", "ALLOW_USER_SRP_AUTH", "ALLOW_REFRESH_TOKEN_AUTH", "ALLOW_ADMIN_USER_PASSWORD_AUTH"]
      access_token         = "minutes"
      access_valid         = 60
      id_token             = "minutes"
      id_token_validity    = 60
      refresh_token        = "minutes"
      refresh_valid        = 60
      generate_secret      = false
      default_redirect_uri = "login/oauth2/code/cognito"
    }
  ]
}
