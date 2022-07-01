variable "src" {
  type = list(string)
}

variable "tags" {
  type = object({
    Description = string
  })
}
