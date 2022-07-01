variable "src" {
  type = object({
    backend     = string
    config_key  = string
    role_name   = string
    policy_name = string
  })
}
