variable "src" {
  type = object({
    backend           = string
    config_key_api    = string
    config_key_deploy = string
    security_policy   = string
  })
}
