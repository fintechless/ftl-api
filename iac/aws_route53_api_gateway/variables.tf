variable "src" {
  type = object({
    backend     = string
    config_key  = string
    record_type = string
  })
}
