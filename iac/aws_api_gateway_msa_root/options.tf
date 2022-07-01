resource "aws_api_gateway_method" "opt" {
  rest_api_id   = local.rest_api_id
  resource_id   = local.parent_id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "opt" {
  rest_api_id      = local.rest_api_id
  resource_id      = local.parent_id
  http_method      = aws_api_gateway_method.opt.http_method
  content_handling = "CONVERT_TO_TEXT"
  type             = "MOCK"

  request_templates = {
    "application/json" = "{ \"statusCode\": 200 }"
  }
}

resource "aws_api_gateway_integration_response" "opt" {
  depends_on = [
    aws_api_gateway_integration.opt,
    aws_api_gateway_method.opt,
  ]

  rest_api_id = local.rest_api_id
  resource_id = local.parent_id
  http_method = aws_api_gateway_method.opt.http_method
  status_code = 200
}

resource "aws_api_gateway_method_response" "opt" {
  depends_on = [aws_api_gateway_method.opt]

  rest_api_id = local.rest_api_id
  resource_id = local.parent_id
  http_method = aws_api_gateway_method.opt.http_method
  status_code = 200

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}
