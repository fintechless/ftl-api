variable "src" {
  type = object({
    backend            = string
    config_key_cognito = string
    config_key_lambda  = string
    statement_id       = string
    action             = string
    principal          = string
  })
}
