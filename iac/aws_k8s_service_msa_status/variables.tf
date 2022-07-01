variable "src" {
  type = object({
    backend        = string
    config_key     = string
    msa            = string
    container_port = number
  })
}
