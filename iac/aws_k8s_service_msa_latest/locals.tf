locals {
  dockercontainers = yamldecode(file("${abspath(path.module)}/../../.dockercontainers"))

  ns_name           = data.terraform_remote_state.aws_eks_cluster.outputs.k8s_namespace
  deployment_labels = data.terraform_remote_state.aws_k8s_deployment_msa_latest.outputs.labels

  service_name   = local.dockercontainers.msa[var.src.msa].svc_name
  container_port = var.src.container_port

  metadata = {
    name      = local.service_name
    namespace = local.ns_name
    labels    = merge({ "app.kubernetes.io/name" = local.service_name }, local.k8s_labels)
  }

  spec = {
    ports = [
      {
        port        = local.k8s.port
        target_port = local.k8s.port
        protocol    = "TCP"
        name        = "internal"
      },
      {
        port        = local.container_port
        target_port = local.k8s.port
        protocol    = "TCP"
        name        = "external"
      }
    ]
  }

  config = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key
  }
}
