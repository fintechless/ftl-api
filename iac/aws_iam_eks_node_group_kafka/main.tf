resource "aws_iam_role" "this" {
  count       = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name        = "${var.src.role_name}-${local.ftl_env}"
  description = var.src.description

  assume_role_policy = file("${path.module}/template/assume_policy.json.tpl")
}

resource "aws_iam_role_policy_attachment" "this" {
  count      = (data.aws_region.this.name == local.ftl_active) ? length(var.src.aws_policies) : 0
  policy_arn = element(var.src.aws_policies, count.index)
  role       = aws_iam_role.this[0].name
}
