variable "src" {
  type = object({
    name        = string
    description = string
    vpc_tags    = map(string)

    rules = map(object({
      type        = string
      from_port   = number
      to_port     = number
      protocol    = string
      self        = optional(bool)
      cidr_blocks = optional(list(string))
    }))
  })
}
