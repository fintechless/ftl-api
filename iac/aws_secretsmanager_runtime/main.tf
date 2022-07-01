resource "aws_secretsmanager_secret" "all" {
  for_each = toset(var.src.names)
  name     = each.key
}

resource "aws_secretsmanager_secret_version" "all" {
  for_each      = aws_secretsmanager_secret.all
  secret_id     = each.value.id
  secret_string = jsonencode({})
}
