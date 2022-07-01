resource "kubernetes_ingress_v1" "this" {
  wait_for_load_balancer = true

  metadata {
    name        = local.metadata.name
    namespace   = local.metadata.namespace
    labels      = local.metadata.labels
    annotations = local.metadata.annotations
  }

  spec {
    rule {
      dynamic "http" {
        for_each = local.spec.rules.http

        content {
          dynamic "path" {
            for_each = http.value.paths

            content {
              path = path.value.path

              dynamic "backend" {
                for_each = path.value.backend

                content {
                  service {
                    name = backend.value.service_name
                    port {
                      number = backend.value.service_port
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
