resource "aws_api_gateway_rest_api" "this" {
  name = "${var.src.name}-${local.ftl_env}"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  tags = {
    Name = "${var.src.name}-${local.ftl_env}"
  }
}
