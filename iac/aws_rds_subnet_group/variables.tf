variable "src" {
  type = object({
    backend               = string
    config_key_eks_cluste = string
    name                  = string
    description           = string
  })
}

variable "tags" {
  type = object({
    Name        = string
    Description = string
  })
}
