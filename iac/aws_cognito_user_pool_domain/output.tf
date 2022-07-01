output "cloudfront_distribution_arn" {
  value = aws_cognito_user_pool_domain.this.cloudfront_distribution_arn
}

output "domain" {
  value     = aws_cognito_user_pool_domain.this.domain
  sensitive = true
}
