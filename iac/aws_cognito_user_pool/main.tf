resource "aws_cognito_user_pool" "this" {
  name              = "${var.src.user_pool_name}-${local.ftl_env}"
  mfa_configuration = var.src.mfa_configuration

  account_recovery_setting {
    recovery_mechanism {
      name     = var.src.account_recovery_setting.recovery_mechanism.name
      priority = tonumber(var.src.account_recovery_setting.recovery_mechanism.priority)
    }
  }

  password_policy {
    minimum_length                   = tonumber(var.src.password_policy.minimum_length)
    require_lowercase                = tobool(var.src.password_policy.require_lowercase)
    require_numbers                  = tobool(var.src.password_policy.require_numbers)
    require_symbols                  = tobool(var.src.password_policy.require_symbols)
    require_uppercase                = tobool(var.src.password_policy.require_uppercase)
    temporary_password_validity_days = tonumber(var.src.password_policy.temporary_password_validity_days)
  }

  admin_create_user_config {
    allow_admin_create_user_only = var.src.admin_create_user_config.allow_admin_create_user_only
    invite_message_template {
      email_message = var.src.admin_create_user_config.email_message
      email_subject = var.src.admin_create_user_config.email_subject
      sms_message   = var.src.admin_create_user_config.sms_message
    }
  }

  email_configuration {
    source_arn = local.email_configuration_source
  }

  lambda_config {
    pre_token_generation = data.terraform_remote_state.aws_lambda_user_pool.outputs.arn
  }

  username_attributes      = var.src.username_attributes
  auto_verified_attributes = var.src.auto_verified_attributes

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_secretsmanager_secret_version" "this" {
  depends_on = [aws_cognito_user_pool.this]
  secret_id  = data.aws_secretsmanager_secret.this.id
  secret_string = jsonencode(merge(local.ftl_cicd_secret_map, {
    AWS_COGNITO_USER_POOL_ID = aws_cognito_user_pool.this.id
  }))
}
