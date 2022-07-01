variable "src" {
  type = object({
    backend        = string
    config_key_eks = string
    config_key_k8s = string
  })
}

variable "tags" {
  type = object({
    Description = string
  })
}
