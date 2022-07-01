output "name" {
  value = aws_db_subnet_group.this.name
}

output "availability_zones" {
  value = [for s in data.aws_subnet.this : s.availability_zone]
}
