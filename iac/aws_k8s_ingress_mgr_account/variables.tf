variable "src" {
  type = object({
    backend        = string
    config_key     = string
    mgr            = string
    image_version  = string
    container_port = number
  })
}
