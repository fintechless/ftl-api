terraform {
  backend "s3" {
    bucket               = "ftl-api-deploy-default-us-east-1-123456789012"
    key                  = "terraform/fintechless/ftl-api/aws_route53_api_gateway/terraform.tfstate"
    region               = "us-east-1"
    workspace_key_prefix = "terraform_workspaces"
  }
}
