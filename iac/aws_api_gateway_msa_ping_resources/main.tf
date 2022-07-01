resource "aws_api_gateway_resource" "this" {
  for_each    = var.gateway_resource
  rest_api_id = local.rest_api_id
  parent_id   = local.parent_id
  path_part   = each.value.path_part
}

resource "aws_api_gateway_method" "this" {
  for_each             = aws_api_gateway_resource.this
  rest_api_id          = local.rest_api_id
  resource_id          = each.value.id
  authorizer_id        = local.authorizer_id
  http_method          = try(var.method[each.key].http_method, null)
  authorization        = try(var.method[each.key].authorization, null)
  authorization_scopes = try(var.method[each.key].authorization_scopes, null)
}

resource "aws_api_gateway_integration" "this" {
  depends_on = [aws_api_gateway_method.this]

  for_each                = aws_api_gateway_resource.this
  rest_api_id             = local.rest_api_id
  resource_id             = each.value.id
  connection_id           = local.connection_id
  type                    = try(var.integration[each.key].type, null)
  passthrough_behavior    = try(var.integration[each.key].passthrough_behavior, null)
  connection_type         = try(var.integration[each.key].connection_type, null)
  http_method             = try(var.integration[each.key].http_method, null)
  integration_http_method = try(var.integration[each.key].integration_http_method, null)
  uri                     = try(format("https://%s/%s", local.ftl_fqdn_api, var.integration[each.key].uri), null)

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

resource "aws_api_gateway_method_response" "this" {
  depends_on = [null_resource.this]

  for_each    = aws_api_gateway_resource.this
  rest_api_id = local.rest_api_id
  resource_id = each.value.id
  http_method = try(var.response[each.key].http_method, null)
  status_code = try(var.response[each.key].status_code, null)

  response_models = {
    "application/json" = "Empty"
  }

  response_parameters = {
    "method.response.header.Access-Control-Allow-Headers" = true
    "method.response.header.Access-Control-Allow-Methods" = true
    "method.response.header.Access-Control-Allow-Origin"  = true
  }
}
