variable "src" {
  type = object({
    backend       = string
    config_key    = string
    function_name = string
    description   = string
    bucket_name   = string
    handler       = string
    runtime       = string
    s3_path       = string
    s3_file       = string
    retention     = string
  })
}
