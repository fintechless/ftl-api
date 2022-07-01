resource "aws_iam_role" "this" {
  count              = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name               = "${var.src.role_name}-${local.ftl_env}"
  assume_role_policy = templatefile("${path.module}/template/assume_policy.json.tpl", {})
}

resource "aws_iam_role_policy" "this" {
  count  = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name   = "${var.src.policy_name}-${local.ftl_env}"
  role   = aws_iam_role.this[0].name
  policy = templatefile("${path.module}/template/trust_policy.json.tpl", {})
}
