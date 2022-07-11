data "aws_region" "this" {}
data "aws_caller_identity" "this" {}
# data "aws_organizations_organization" "this" {}

data "aws_secretsmanager_secret" "this" {
  name = var.FTL_SECRET_CICD
}

data "aws_secretsmanager_secret_version" "this" {
  secret_id = data.aws_secretsmanager_secret.this.id
}

data "terraform_remote_state" "aws_eks_cluster" {
  backend = "s3"
  config = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = local.ftl_tfstate
  }
}

terraform {
  required_version = ">= 0.12.0, < 1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.20.1"
    }

    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "2.11.0"
    }

    kubectl = {
      source  = "gavinbunney/kubectl"
      version = "1.14.0"
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

provider "kubernetes" {
  host                   = local.k8s.host
  cluster_ca_certificate = local.k8s.cert

  exec {
    api_version = "client.authentication.k8s.io/v1alpha1"
    args        = ["eks", "get-token", "--cluster-name", local.k8s.cluster]
    command     = "aws"
  }
}

provider "kubectl" {
  host                   = local.k8s.host
  cluster_ca_certificate = local.k8s.cert

  exec {
    api_version = "client.authentication.k8s.io/v1alpha1"
    args        = ["eks", "get-token", "--cluster-name", local.k8s.cluster]
    command     = "aws"
  }
}

locals {
  ftl_env              = terraform.workspace
  ftl_cicd_secret_name = var.FTL_SECRET_CICD
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

  ftl_active_subnets  = nonsensitive(local.ftl_cicd_secret_map["FTL_ACTIVE_SUBNETS"])
  ftl_passive_subnets = nonsensitive(local.ftl_cicd_secret_map["FTL_PASSIVE_SUBNETS"])

  ftl_domain         = local.ftl_cicd_secret_map["FTL_DOMAIN"]
  ftl_subdomain_api  = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_API"]
  ftl_subdomain_app  = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_APP"]
  ftl_subdomain_auth = local.ftl_cicd_secret_map["FTL_SUBDOMAIN_AUTH"]
  ftl_fqdn_api       = local.ftl_cicd_secret_map["FTL_FQDN_API"]
  ftl_fqdn_app       = local.ftl_cicd_secret_map["FTL_FQDN_APP"]
  ftl_fqdn_auth      = local.ftl_cicd_secret_map["FTL_FQDN_AUTH"]

  k8s = {
    cluster   = try(data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name, null)
    host      = try(data.terraform_remote_state.aws_eks_cluster.outputs.k8s_endpoint, local.ftl_env)
    cert      = try(base64decode(data.terraform_remote_state.aws_eks_cluster.outputs.k8s_certificate), null)
    namespace = try(data.terraform_remote_state.aws_eks_cluster.outputs.k8s_namespace, null)
    version   = try(data.terraform_remote_state.aws_eks_cluster.outputs.k8s_version, null)
    port      = try(data.terraform_remote_state.aws_eks_cluster.outputs.k8s_port, null)
  }

  k8s_labels = {
    "app.kubernetes.io/part-of"     = local.k8s.namespace
    "app.kubernetes.io/version"     = local.k8s.version
    "app.kubernetes.io/environment" = local.ftl_env
  }

  k8s_default_envs = [
    {
      name  = "AWS_ACCOUNT_ID"
      value = data.aws_caller_identity.this.account_id
    },
    {
      name  = "FTL_CLOUD_REGION_PRIMARY"
      value = local.ftl_active
    },
    {
      name  = "FTL_CLOUD_REGION_SECONDARY"
      value = local.ftl_passive
    },
    {
      name  = "FTL_CLOUD_PROVIDER"
      value = "aws"
    },
    {
      name  = "FTL_ENVIRONMENT"
      value = local.ftl_env
    },
    {
      name  = "FTL_DEPLOYMENT_ID"
      value = "ftl-local"
    },
    {
      name  = "FTL_DEPLOY_BUCKET"
      value = local.ftl_bucket
    },
    {
      name  = "FTL_RUNTIME_BUCKET"
      value = local.ftl_cicd_secret_map["FTL_RUNTIME_BUCKET"]
    },
  ]
}

variable "FTL_SECRET_CICD" {
  type    = string
  default = "FTL_SECRET_CICD_DEFAULT"
}

variable "FTL_ALLOWED_AWS_ACCOUNTS" {
  type    = string
  default = null
}
