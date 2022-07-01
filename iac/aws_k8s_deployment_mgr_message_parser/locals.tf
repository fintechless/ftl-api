locals {
  dockercontainers = yamldecode(file("${abspath(path.module)}/../../.dockercontainers"))

  cluster_name            = data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name
  cluster_node_group_name = data.terraform_remote_state.aws_eks_node_group_api.outputs.node_group_name
  ns_name                 = data.terraform_remote_state.aws_eks_cluster.outputs.k8s_namespace
  ecr_repository_url      = data.terraform_remote_state.aws_ecr_repository.outputs.url.message-parser

  replicas        = var.src.replicas
  image_version   = var.src.image_version
  container_name  = local.dockercontainers.mgr[var.src.mgr].name
  deployment_name = local.dockercontainers.mgr[var.src.mgr].dpl_name
  container_port  = local.k8s.port

  metadata = {
    name      = local.deployment_name
    namespace = local.ns_name
    labels    = merge({ "app.kubernetes.io/name" = local.deployment_name }, local.k8s_labels)
  }

  spec = {
    replicas = local.replicas

    selector = {
      match_labels = local.metadata.labels
    }

    strategy = {
      type = "RollingUpdate"
      rolling_update = {
        max_surge       = 2
        max_unavailable = 1
      }
    }

    template = {
      metadata = { labels = local.metadata.labels }
    }

    containers = [
      {
        name              = local.deployment_name
        image             = "${local.ecr_repository_url}:${local.image_version}"
        image_pull_policy = "Always"
        container_port    = local.container_port
        # port_name         = local.deployment_name
        envs = concat(
          local.k8s_default_envs,
          [{
            name  = "LD_LIBRARY_PATH"
            value = "/usr/local/lib"
            }, {
            name  = "FLASK_ENV"
            value = local.ftl_env
            }, {
            name  = "FLASK_APP"
            value = local.container_name
            }, {
            name  = "FLASK_RUN_PORT"
            value = local.container_port
            }, {
            name  = "FLASK_RUN_HOST"
            value = "0.0.0.0"
            }, {
            name  = "FTL_ENVIRON_CONTEXT_SECRET"
            value = local.ftl_cicd_secret_name
        }])
        volume_mount = {
          name       = "tz-config"
          mount_path = "/etc/localtime"
        }
      }
    ]

    volumes = [
      {
        name = "tz-config"
        path = "/usr/share/zoneinfo/America/New_York"
      }
    ]

    tolerations = [
      {
        key      = "reserved-pool"
        value    = "true"
        operator = "Equal"
        effect   = "NoSchedule"
      }
    ]

    affinity = [{
      node_affinity = [
        {
          required_during_scheduling_ignored_during_execution = [
            {
              node_selector_term = [
                {
                  match_expressions = [
                    {
                      key      = "eks.amazonaws.com/nodegroup"
                      operator = "In"
                      values   = [local.cluster_node_group_name]
                    }
                  ]
                }
              ]
            }
          ]
        }
      ]

      pod_anti_affinity = [
        {
          required_during_scheduling_ignored_during_execution = [
            {
              label_selector = [
                {
                  match_expressions = [
                    {
                      key      = "app.kubernetes.io/name"
                      operator = "In"
                      values   = [local.deployment_name]
                    }
                  ]
                }
              ]

              topology_key = "kubernetes.io/hostname"
            }
          ]
        }
      ]
    }]
  }

  config_ecr = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_ecr
  }

  config_node = {
    region = data.aws_region.this.name
    bucket = local.ftl_bucket
    key    = var.src.config_key_node
  }
}
