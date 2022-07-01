resource "aws_api_gateway_resource" "this" {
  rest_api_id = local.rest_api_id
  parent_id   = local.parent_id
  path_part   = var.src.uri_path
}

resource "aws_api_gateway_method" "this" {
  rest_api_id          = local.rest_api_id
  resource_id          = aws_api_gateway_resource.this.id
  authorizer_id        = local.authorizer_id
  http_method          = var.src.http_method
  authorization        = var.src.authorization
  authorization_scopes = ["api/public.read"]
}

resource "aws_api_gateway_integration" "this" {
  depends_on = [aws_api_gateway_method.this]

  rest_api_id             = local.rest_api_id
  resource_id             = aws_api_gateway_resource.this.id
  connection_id           = local.connection_id
  type                    = var.src.type
  passthrough_behavior    = var.src.passthrough_behavior
  connection_type         = var.src.connection_type
  http_method             = var.src.http_method
  integration_http_method = var.src.integration_http_method
  uri                     = format("http://%s:%s/%s/%s", local.lb_dns_name, local.msa_port, var.src.uri_prefix, var.src.uri_path)

  request_templates = {
    "application/json" = "{ \"statusCode\": 200 }"
  }
}

resource "null_resource" "this" {
  triggers = {
    response = aws_api_gateway_method.this.resource_id
  }

  provisioner "local-exec" {
    command = "sleep 5"
  }
}

resource "aws_api_gateway_method_response" "this" {
  depends_on = [null_resource.this]

  rest_api_id = local.rest_api_id
  resource_id = aws_api_gateway_resource.this.id
  http_method = var.src.http_method
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
