resource "aws_iam_role" "this" {
  count = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name  = "${var.src.role_name}-${local.ftl_env}"
  path  = var.src.path

  assume_role_policy = templatefile("${path.module}/template/assume_policy.json.tpl", {})
}
