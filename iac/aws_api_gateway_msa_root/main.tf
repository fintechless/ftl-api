resource "aws_api_gateway_method" "this" {
  for_each             = var.method
  rest_api_id          = local.rest_api_id
  resource_id          = local.parent_id
  authorizer_id        = local.authorizer_id
  http_method          = each.value.http_method
  authorization_scopes = each.value.authorization_scopes
  authorization        = each.value.authorization
}

resource "aws_api_gateway_integration" "this" {
  depends_on = [aws_api_gateway_method.this]

  for_each                = var.integration
  rest_api_id             = local.rest_api_id
  resource_id             = local.parent_id
  connection_id           = local.connection_id
  type                    = each.value.type
  passthrough_behavior    = each.value.passthrough_behavior
  connection_type         = each.value.connection_type
  http_method             = each.value.http_method
  integration_http_method = each.value.integration_http_method
  uri                     = format("http://%s:%s/%s", local.lb_dns_name, local.msa_port[each.key], each.value.uri)

  request_templates = {
    "application/json" = "{ \"statusCode\": 200 }"
  }
}

resource "null_resource" "this" {
  for_each = aws_api_gateway_method.this
  triggers = {
    response = each.value.resource_id
  }

  provisioner "local-exec" {
    command = "sleep 5"
  }
}

resource "aws_api_gateway_method_response" "response" {
  depends_on = [null_resource.this]

  for_each    = var.method
  rest_api_id = local.rest_api_id
  resource_id = local.parent_id
  http_method = each.value.http_method
  status_code = "200"

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}
