variable "src" {
  type = object({
    backend        = string
    config_key     = string
    mgr            = string
    container_port = number
  })
}
