variable "src" {
  type = object({
    backend            = string
    config_key_api     = string
    config_key_default = string
    config_key_kafka   = string
  })
}
