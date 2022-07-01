resource "kubernetes_deployment" "this" {
  metadata {
    name      = local.metadata.name
    namespace = local.metadata.namespace
    labels    = local.metadata.labels
  }

  spec {
    replicas = local.spec.replicas

    selector {
      match_labels = local.spec.selector.match_labels
    }

    strategy {
      type = local.spec.strategy.type
      rolling_update {
        max_surge       = local.spec.strategy.rolling_update.max_surge
        max_unavailable = local.spec.strategy.rolling_update.max_unavailable
      }
    }

    template {
      metadata {
        labels = local.metadata.labels
      }

      spec {
        dynamic "toleration" {
          for_each = local.spec.tolerations

          content {
            key      = toleration.value.key
            value    = toleration.value.value
            operator = toleration.value.operator
            effect   = toleration.value.effect
          }
        }

        dynamic "affinity" {
          for_each = local.spec.affinity

          content {
            dynamic "node_affinity" {
              for_each = affinity.value.node_affinity

              content {
                dynamic "required_during_scheduling_ignored_during_execution" {
                  for_each = node_affinity.value.required_during_scheduling_ignored_during_execution

                  content {
                    dynamic "node_selector_term" {
                      for_each = required_during_scheduling_ignored_during_execution.value.node_selector_term

                      content {
                        dynamic "match_expressions" {
                          for_each = node_selector_term.value.match_expressions

                          content {
                            key      = match_expressions.value.key
                            operator = match_expressions.value.operator
                            values   = match_expressions.value.values
                          }
                        }
                      }
                    }
                  }
                }
              }
            }

            dynamic "pod_anti_affinity" {
              for_each = affinity.value.pod_anti_affinity

              content {
                dynamic "required_during_scheduling_ignored_during_execution" {
                  for_each = pod_anti_affinity.value.required_during_scheduling_ignored_during_execution

                  content {
                    dynamic "label_selector" {
                      for_each = required_during_scheduling_ignored_during_execution.value.label_selector

                      content {
                        dynamic "match_expressions" {
                          for_each = label_selector.value.match_expressions
                          content {
                            key      = match_expressions.value.key
                            operator = match_expressions.value.operator
                            values   = match_expressions.value.values
                          }
                        }
                      }
                    }
                    topology_key = required_during_scheduling_ignored_during_execution.value.topology_key
                  }
                }
              }
            }
          }
        }

        dynamic "container" {
          for_each = local.spec.containers

          content {
            name              = container.value.name
            image             = container.value.image
            image_pull_policy = container.value.image_pull_policy
            command           = ["/bin/bash", "-c"]
            args = [
              templatefile("${path.module}/template/run.sh.tpl", {})
            ]

            # port {
            # container_port = container.value.container_port
            # name           = container.value.port_name
            # }
            dynamic "env" {
              for_each = container.value.envs
              content {
                name  = env.value.name
                value = env.value.value
              }
            }

            volume_mount {
              name       = container.value.volume_mount.name
              mount_path = container.value.volume_mount.mount_path
            }
          }
        }
        dynamic "volume" {
          for_each = local.spec.volumes

          content {
            name = volume.value.name

            host_path {
              path = volume.value.path
            }
          }
        }
      }
    }
  }
}
