variable "src" {
  type = object({
    backend                 = string
    config_key_api          = string
    config_key_auth         = string
    config_key_link         = string
    config_key_lb           = string
    config_key_tg_ping      = string
    config_key_tg_msg       = string
    passthrough_behavior    = string
    authorization           = string
    type                    = string
    connection_type         = string
    http_method             = string
    integration_http_method = string
    uri_prefix              = string
    uri_path                = string
  })
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
