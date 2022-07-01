variable "src" {
  type = object({
    backend    = string
    config_key = string
    user_groups = list(object({
      name                 = string
      description          = string
      allowed_oauth_flows  = list(string)
      allowed_oauth_scopes = list(string)
      explicit_auth_flows  = list(string)
      id_token             = optional(string)
      id_token_validity    = optional(string)
      access_token         = optional(string)
      access_valid         = optional(number)
      refresh_token        = optional(string)
      refresh_valid        = optional(number)
      generate_secret      = bool
      read_attributes      = optional(list(string))
      write_attributes     = optional(list(string))
      default_redirect_uri = optional(string)
    }))
  })
}
