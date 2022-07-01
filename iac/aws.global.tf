data "aws_region" "this" {}
data "aws_caller_identity" "this" {}
data "aws_organizations_organization" "this" {}

data "aws_secretsmanager_secret" "this" {
  name = var.FTL_CICD_SECRET
}

data "aws_secretsmanager_secret_version" "this" {
  secret_id = data.aws_secretsmanager_secret.this.id
}

terraform {
  required_version = ">= 0.12.0, < 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.20.1"
    }
  }
}

provider "aws" {
  allowed_account_ids = try(split(",", var.FTL_ALLOWED_AWS_ACCOUNTS), null)

  default_tags {
    tags = {
      Environment  = local.ftl_env
      Microservice = "ftl-api"
      Contact      = "hello@fintechless.com"
    }
  }
}

locals {
  ftl_env              = terraform.workspace
  ftl_cicd_secret_name = var.FTL_CICD_SECRET
  ftl_cicd_secret_map  = jsondecode(data.aws_secretsmanager_secret_version.this.secret_string)

  ftl_bucket  = local.ftl_cicd_secret_map["FTL_TFSTATE_BUCKET"]
  ftl_tfstate = local.ftl_cicd_secret_map["FTL_TFSTATE_OBJECT"]

  ftl_active  = local.ftl_cicd_secret_map["FTL_ACTIVE_REGION"]
  ftl_passive = local.ftl_cicd_secret_map["FTL_PASSIVE_REGION"]

  ftl_region = tomap({
    "${local.ftl_active}"  = "active"
    "${local.ftl_passive}" = "passive"
  })

  ftl_vpc = tomap({
    "${local.ftl_active}"  = local.ftl_cicd_secret_map["FTL_ACTIVE_VPC"]
    "${local.ftl_passive}" = local.ftl_cicd_secret_map["FTL_PASSIVE_VPC"]
  })

  ftl_domain         = local.ftl_cicd_secret_map["FTL_DOMAIN"]
  ftl_subdomain_api  = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_API"]
  ftl_subdomain_app  = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_APP"]
  ftl_subdomain_auth = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_AUTH"]
  ftl_fqdn_api       = local.ftl_cicd_secret_map["FTL_FQDN_API"]
  ftl_fqdn_app       = local.ftl_cicd_secret_map["FTL_FQDN_APP"]
  ftl_fqdn_auth      = local.ftl_cicd_secret_map["FTL_FQDN_AUTH"]
}

variable "FTL_CICD_SECRET" {
  type    = string
  default = "ftl-cicd-secret"
}

variable "FTL_ALLOWED_AWS_ACCOUNTS" {
  type    = string
  default = null
}
