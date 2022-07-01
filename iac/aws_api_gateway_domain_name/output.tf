output "domain_name" {
  value     = local.ftl_domain == "" ? null : aws_api_gateway_domain_name.this[0].domain_name
  sensitive = true
}

output "regional_domain_name" {
  value = local.ftl_domain == "" ? null : aws_api_gateway_domain_name.this[0].regional_domain_name
}

output "regional_zone_id" {
  value = local.ftl_domain == "" ? null : aws_api_gateway_domain_name.this[0].regional_zone_id
}
