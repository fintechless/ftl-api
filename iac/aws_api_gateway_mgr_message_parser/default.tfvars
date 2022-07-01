src = {
  backend               = "s3"
  config_key_api        = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"
  config_key_parent_api = "terraform/fintechless/ftl-api/aws_api_gateway_mgr_message/terraform.tfstate"
  config_key_auth       = "terraform/fintechless/ftl-api/aws_api_gateway_authorizer/terraform.tfstate"
  config_key_link       = "terraform/fintechless/ftl-api/aws_api_gateway_vpc_link_mgr/terraform.tfstate"
  config_key_lb         = "terraform/fintechless/ftl-api/aws_lb_mgr/terraform.tfstate"
  config_key_tg         = "terraform/fintechless/ftl-api/aws_lb_target_group_mgr_message_parser/terraform.tfstate"

  passthrough_behavior = "WHEN_NO_MATCH"
  authorization        = "COGNITO_USER_POOLS"
  type                 = "HTTP_PROXY"
  connection_type      = "VPC_LINK"
  uri_prefix           = "mgr"
  uri_path             = "message/parser"
  resource_path        = "parser"
  http_methods = [
    {
      http_method             = "GET"
      integration_http_method = "GET"
    },
    {
      http_method             = "PATCH"
      integration_http_method = "PATCH"
    }
  ]
}
