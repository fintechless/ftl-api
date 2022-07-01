variable "src" {
  type = object({
    backend        = string
    config_key_eks = string
    config_key_iam = string
    role_name      = string
    policy_name    = string
    description    = string
    path           = string
  })
}
