variable "src" {
  type = object({
    backend    = string
    config_key = string
    name       = string
    identifier = string
  })
}

variable "scopes" {
  type = list(object({
    name        = string
    description = string
  }))
}
