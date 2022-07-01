variable "src" {
  type = object({
    backend                          = string
    config_key_cognito               = string
    config_key_client                = string
    config_key_iam                   = string
    allow_unauthenticated_identities = string
    allow_classic_flow               = string
  })
}
