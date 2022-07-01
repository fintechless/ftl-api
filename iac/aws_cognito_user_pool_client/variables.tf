variable "src" {
  type = object({
    backend                              = string
    config_key_cognito                   = string
    config_key_user_group                = string
    config_key_resource                  = string
    prevent_user_existence_errors        = string
    allowed_oauth_flows_user_pool_client = string
    supported_identity_providers         = list(string)
  })
}
