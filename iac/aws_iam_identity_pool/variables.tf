variable "src" {
  type = object({
    backend            = string
    config_key_cognito = string
    config_key_iam     = string
    description        = string
    path               = string
  })
}
