resource "aws_api_gateway_account" "this" {
  cloudwatch_role_arn = data.terraform_remote_state.aws_iam_api_gateway.outputs.arn
}
