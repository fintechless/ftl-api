src = {
  backend         = "s3"
  config_key_api  = "terraform/fintechless/ftl-api/aws_api_gateway_rest_api/terraform.tfstate"
  config_key_auth = "terraform/fintechless/ftl-api/aws_api_gateway_authorizer/terraform.tfstate"
  config_key_link = "terraform/fintechless/ftl-api/aws_api_gateway_vpc_link_msa/terraform.tfstate"
  config_key_lb   = "terraform/fintechless/ftl-api/aws_lb_msa/terraform.tfstate"
  config_key_tg   = "terraform/fintechless/ftl-api/aws_lb_target_group_msa_status/terraform.tfstate"

  passthrough_behavior    = "WHEN_NO_MATCH"
  authorization           = "COGNITO_USER_POOLS"
  type                    = "HTTP_PROXY"
  connection_type         = "VPC_LINK"
  http_method             = "GET"
  integration_http_method = "GET"
  uri_prefix              = "msa"
  uri_path                = "status"
}
