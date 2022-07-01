variable "src" {
  type = object({
    name                 = string
    authorizer_name      = string
    rest_api_description = string
  })
}
