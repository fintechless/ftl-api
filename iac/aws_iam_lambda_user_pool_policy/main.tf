resource "aws_iam_policy" "this" {
  count       = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name        = "${var.src.policy_name}-${local.ftl_env}"
  description = var.src.description
  path        = var.src.path

  policy = templatefile("${path.module}/template/trust_policy.json.tpl", {
    user_pool_arn = data.terraform_remote_state.aws_cognito_user_pool.outputs.arn
  })
}

resource "aws_iam_role_policy_attachment" "this" {
  count      = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  role       = data.terraform_remote_state.aws_iam_lambda_user_pool.outputs.name
  policy_arn = aws_iam_policy.this[0].arn
}
