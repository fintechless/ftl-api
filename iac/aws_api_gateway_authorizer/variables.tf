variable "src" {
  type = object({
    backend            = string
    config_key_api     = string
    config_key_cognito = string
    name               = string
    type               = string
    identity_source    = string
  })
}
