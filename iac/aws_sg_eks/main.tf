resource "aws_security_group" "this" {
  name        = "${var.src.name}-${local.ftl_env}"
  description = var.src.description
  vpc_id      = data.aws_vpc.this.id

  tags = {
    Name = "${var.src.name}-${local.ftl_env}"
  }

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_security_group_rule" "this" {
  for_each          = var.src.rules
  type              = each.value.type
  from_port         = each.value.from_port
  to_port           = each.value.to_port
  protocol          = each.value.protocol
  self              = try(each.value.self, false)
  cidr_blocks       = try(each.value.cidr_blocks, [])
  security_group_id = aws_security_group.this.id
}
