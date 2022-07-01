resource "aws_iam_role" "this" {
  for_each = (data.aws_region.this.name == local.ftl_active) ? data.terraform_remote_state.user_pool_client.outputs.ids : null

  name = "${each.key}-cognito-identity-role-${local.ftl_env}"
  path = var.src.path

  assume_role_policy = templatefile("${path.module}/template/assume_policy.json.tpl", {
    identity_pool_id = each.value
  })
}

resource "aws_iam_policy" "this" {
  for_each = (data.aws_region.this.name == local.ftl_active) ? data.terraform_remote_state.user_pool_client.outputs.ids : null

  name        = "${each.key}-cognito-identity-policy-${local.ftl_env}"
  description = var.src.description
  path        = var.src.path
  policy      = templatefile("${path.module}/template/trust_policy.json.tpl", {})
}

resource "aws_iam_role_policy_attachment" "this" {
  for_each = (data.aws_region.this.name == local.ftl_active) ? data.terraform_remote_state.user_pool_client.outputs.ids : null

  role       = aws_iam_role.this[each.key].name
  policy_arn = aws_iam_policy.this[each.key].arn
}
