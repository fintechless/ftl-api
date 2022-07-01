locals {
  dockercontainers = yamldecode(file("${abspath(path.module)}/../../.dockercontainers"))

  deployment_labels = data.terraform_remote_state.aws_k8s_deployment_mgr_message_definition.outputs.labels
  eks_sg_ids        = data.terraform_remote_state.aws_eks_cluster.outputs.security_group_ids
  eks_subnet_ids    = data.terraform_remote_state.aws_eks_cluster.outputs.subnet_ids
  ns_name           = data.terraform_remote_state.aws_eks_cluster.outputs.k8s_namespace
  alb_name          = data.terraform_remote_state.aws_eks_cluster.outputs.alb_name

  ingress_name      = local.dockercontainers.mgr[var.src.mgr].igr_name
  service_name      = local.dockercontainers.mgr[var.src.mgr].svc_name
  image_version     = var.src.image_version
  container_port    = var.src.container_port
  health_check_path = local.dockercontainers.mgr[var.src.mgr].health_check_path

  metadata = {
    name      = local.ingress_name
    namespace = local.ns_name
    labels    = merge({ "app.kubernetes.io/name" = local.ingress_name }, local.k8s_labels)
    annotations = {
      "kubernetes.io/ingress.class"                  = "alb"
      "alb.ingress.kubernetes.io/load-balancer-name" = local.alb_name
      "alb.ingress.kubernetes.io/group.name"         = local.alb_name
      "alb.ingress.kubernetes.io/scheme"             = "internal"
      "alb.ingress.kubernetes.io/target-type"        = "ip"
      "alb.ingress.kubernetes.io/healthcheck-path"   = local.health_check_path
      "alb.ingress.kubernetes.io/listen-ports"       = "${jsonencode([{ "HTTP" : local.container_port }])}"
      "alb.ingress.kubernetes.io/security-groups"    = replace(join(", ", local.eks_sg_ids), " ", "")
      "alb.ingress.kubernetes.io/subnets"            = replace(join(", ", local.eks_subnet_ids), " ", "")
    }
  }

  spec = {
    rules = {
      http = [
        {
          paths = [
            {
              path = "/*"
              backend = [
                {
                  service_name = local.service_name
                  service_port = local.container_port
                }
              ]
            }
          ]
        }
      ]
    }
  }

  config = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key
  }
}
