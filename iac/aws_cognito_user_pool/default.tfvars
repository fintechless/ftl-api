src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_lambda_user_pool/terraform.tfstate"

  user_pool_name           = "ftl-cognito-user-pool"
  mfa_configuration        = "OFF"
  username_attributes      = ["email"]
  auto_verified_attributes = ["email"]

  account_recovery_setting = {
    recovery_mechanism = {
      name     = "verified_email"
      priority = "1"
    }
  }

  password_policy = {
    minimum_length                   = "8"
    require_lowercase                = "true"
    require_numbers                  = "true"
    require_symbols                  = "true"
    require_uppercase                = "true"
    temporary_password_validity_days = "7"
  }

  admin_create_user_config = {
    allow_admin_create_user_only = true
    email_message                = <<EOT
      Hello,
      <br/><br/>
      You have been invited to join Fintechless Platform. Here below are your private credentials to be used to login:
      <br/><br/>
      * Username: {username}
      <br/>
      * Password: {####}
      <br/><br/>
      Thank you,
      <br/>
      Administration.
    EOT
    email_subject                = "You are invited to join Fintechless Platform"
    sms_message                  = "You have been invited to join Fintechless Platform. Your username is {username} and temporary password is {####}."
  }

  email_configuration = {
    name = "hello@fintechless.com"
  }
}
