variable "src" {
  type = object({
    backend           = string
    config_key        = string
    description       = string
    stage_description = string
    stage_name        = string
    retention_in_days = string
    name_prefix       = string
  })
}
