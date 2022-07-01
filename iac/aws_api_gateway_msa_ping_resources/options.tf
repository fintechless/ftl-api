resource "aws_api_gateway_method" "opt" {
  for_each      = aws_api_gateway_resource.this
  rest_api_id   = local.rest_api_id
  resource_id   = each.value.id
  http_method   = "OPTIONS"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "opt" {
  depends_on = [aws_api_gateway_method.opt]

  for_each         = aws_api_gateway_resource.this
  rest_api_id      = local.rest_api_id
  resource_id      = each.value.id
  http_method      = "OPTIONS"
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

  for_each    = aws_api_gateway_resource.this
  rest_api_id = local.rest_api_id
  resource_id = each.value.id
  http_method = "OPTIONS"
  status_code = 200
}

resource "aws_api_gateway_method_response" "opt" {
  depends_on = [aws_api_gateway_method.this]

  for_each    = aws_api_gateway_resource.this
  rest_api_id = local.rest_api_id
  resource_id = each.value.id
  http_method = "OPTIONS"
  status_code = 200

  response_models = {
    "application/json" = "Empty"
  }
}
