variable "src" {
  type = object({
    backend         = string
    config_key_ecr  = string
    config_key_node = string
    mgr             = string
    replicas        = string
    image_version   = string
  })
}
