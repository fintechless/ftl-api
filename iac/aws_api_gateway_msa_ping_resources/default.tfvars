src = {
  backend         = "s3"
  config_key_api  = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"
  config_key_auth = "terraform/fintechless/ftl-api/aws_api_gateway_authorizer/terraform.tfstate"
  config_key_link = "terraform/fintechless/ftl-api/aws_api_gateway_vpc_link_msa/terraform.tfstate"
  config_key_msa  = "terraform/fintechless/ftl-api/aws_api_gateway_msa_ping/terraform.tfstate"
}

gateway_resource = {
  ping_cache = {
    path_part = "cache"
  }

  ping_nosql = {
    path_part = "nosql"
  }

  ping_sql = {
    path_part = "sql"
  }

  ping_storage = {
    path_part = "storage"
  }
}

method = {
  ping_cache = {
    http_method          = "GET"
    authorization        = "COGNITO_USER_POOLS"
    authorization_scopes = ["api/public.read"]
  }

  ping_nosql = {
    http_method          = "GET"
    authorization        = "COGNITO_USER_POOLS"
    authorization_scopes = ["api/public.read"]
  }

  ping_sql = {
    http_method          = "GET"
    authorization        = "COGNITO_USER_POOLS"
    authorization_scopes = ["api/public.read"]
  }

  ping_storage = {
    http_method          = "GET"
    authorization        = "COGNITO_USER_POOLS"
    authorization_scopes = ["api/public.read"]
  }
}

integration = {
  ping_cache = {
    type                    = "HTTP_PROXY"
    passthrough_behavior    = "WHEN_NO_MATCH"
    connection_type         = "VPC_LINK"
    http_method             = "GET"
    integration_http_method = "GET"
    uri                     = "ping/cache"
  }

  ping_nosql = {
    type                    = "HTTP_PROXY"
    passthrough_behavior    = "WHEN_NO_MATCH"
    connection_type         = "VPC_LINK"
    http_method             = "GET"
    integration_http_method = "GET"
    uri                     = "ping/nosql"
  }

  ping_sql = {
    type                    = "HTTP_PROXY"
    passthrough_behavior    = "WHEN_NO_MATCH"
    connection_type         = "VPC_LINK"
    http_method             = "GET"
    integration_http_method = "GET"
    uri                     = "ping/sql"
  }

  ping_storage = {
    type                    = "HTTP_PROXY"
    passthrough_behavior    = "WHEN_NO_MATCH"
    connection_type         = "VPC_LINK"
    http_method             = "GET"
    integration_http_method = "GET"
    uri                     = "ping/storage"
  }
}

response = {
  ping_cache = {
    http_method = "GET"
    status_code = "200"
  }

  ping_nosql = {
    http_method = "GET"
    status_code = "200"
  }

  ping_sql = {
    http_method = "GET"
    status_code = "200"
  }

  ping_storage = {
    http_method = "GET"
    status_code = "200"
  }
}
