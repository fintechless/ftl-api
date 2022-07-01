variable "src" {
  type = object({
    backend       = string
    config_key_lb = string
    config_key_tg = string
    port          = string
    protocol      = string
  })
}
