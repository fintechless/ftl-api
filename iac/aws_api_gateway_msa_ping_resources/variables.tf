variable "src" {
  type = object({
    backend         = string
    config_key_api  = string
    config_key_auth = string
    config_key_link = string
    config_key_msa  = string
  })
}

variable "gateway_resource" {
  type = map(object({
    path_part = string
  }))
}

variable "method" {
  type = map(object({
    http_method          = string
    authorization        = string
    authorization_scopes = list(string)
  }))
}

variable "integration" {
  type = map(object({
    type                    = string
    passthrough_behavior    = string
    connection_type         = string
    http_method             = string
    integration_http_method = string
    uri                     = string
  }))
}

variable "response" {
  type = map(object({
    http_method = string
    status_code = string
  }))
}
