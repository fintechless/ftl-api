variable "src" {
  type = object({
    backend      = string
    config_key   = string
    role_name    = string
    description  = string
    aws_policies = list(string)
  })
}
