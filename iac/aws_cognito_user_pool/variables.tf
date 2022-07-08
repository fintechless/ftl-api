variable "src" {
  type = object({
    backend                  = string
    config_key               = string
    user_pool_name           = string
    mfa_configuration        = string
    username_attributes      = list(string)
    auto_verified_attributes = list(string)

    account_recovery_setting = object({
      recovery_mechanism = object({
        name     = string
        priority = string
      })
    })

    password_policy = object({
      minimum_length                   = string
      require_lowercase                = string
      require_numbers                  = string
      require_symbols                  = string
      require_uppercase                = string
      temporary_password_validity_days = string
    })

    admin_create_user_config = object({
      allow_admin_create_user_only = bool
      email_message                = string
      email_subject                = string
      sms_message                  = string
    })

    email_configuration = object({
      name = string
    })
  })
}
