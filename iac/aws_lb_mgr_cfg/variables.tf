variable "src" {
  type = object({
    backend            = string
    config_key         = string
    name               = string
    internal           = string
    load_balancer_type = string
  })
}
