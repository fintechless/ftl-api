output "id" {
  value = aws_security_group.this.id
}

output "vpc_id" {
  value     = data.aws_vpc.this.id
  sensitive = true
}
