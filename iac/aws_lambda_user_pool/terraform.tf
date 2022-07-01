terraform {
  backend "s3" {
    bucket               = "ftl-api-deploy-default-us-east-1-123456789012"
    key                  = "terraform/fintechless/ftl-api/aws_lambda_user_pool/terraform.tfstate"
    region               = "us-east-1"
    workspace_key_prefix = "terraform_workspaces"
  }
}
