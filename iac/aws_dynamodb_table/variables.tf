variable "src" {
  type = map(object({
    hash_key         = string
    range_key        = string
    table_name       = string
    billing_mode     = string
    stream_view_type = string

    attributes = list(object({
      name = string
      type = string
    }))

    gsi_configs = list(object({
      name               = string
      hash_key           = string
      range_key          = string
      projection_type    = string
      non_key_attributes = list(string)
    }))

    tags = object({
      Description = string
    })
  }))
}
