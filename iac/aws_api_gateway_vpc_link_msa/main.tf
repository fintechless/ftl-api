resource "aws_api_gateway_vpc_link" "this" {
  name        = "${var.src.name}-${local.ftl_env}"
  target_arns = [data.terraform_remote_state.aws_lb.outputs.arn]
}
