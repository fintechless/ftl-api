src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_cognito_user_pool/terraform.tfstate"

  name       = "api.fintechless"
  identifier = "api"
}

scopes = [
  {
    name        = "public.read"
    description = "Public - Read permissions"
  },
  {
    name        = "public.write"
    description = "Public - Write permissions"
  },
  {
    name        = "private.read"
    description = "Private - Read permissions"
  },
  {
    name        = "private.write"
    description = "Private - Write permissions"
  },
  {
    name        = "mgr.read"
    description = "Management - Read permissions"
  },
  {
    name        = "mgr.write"
    description = "Management - Write permissions"
  },
  {
    name        = "bi.read"
    description = "BI - Read permissions"
  },
  {
    name        = "bi.write"
    description = "BI - Write permissions"
  }
]
