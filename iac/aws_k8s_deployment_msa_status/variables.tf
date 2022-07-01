variable "src" {
  type = object({
    backend         = string
    config_key_ecr  = string
    config_key_node = string
    msa             = string
    replicas        = string
    image_version   = string
  })
}
