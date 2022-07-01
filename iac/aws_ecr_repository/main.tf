resource "aws_ecr_repository" "this" {
  for_each             = toset(var.src)
  name                 = each.key
  image_tag_mutability = "MUTABLE"

  image_scanning_configuration {
    scan_on_push = false
  }

  tags = merge(var.tags, { Name = each.key })
}

resource "aws_ecr_lifecycle_policy" "this" {
  for_each   = toset(var.src)
  repository = aws_ecr_repository.this[each.key].name
  policy     = file("${path.module}/template/lifecycle_policy.json.tpl")
}
