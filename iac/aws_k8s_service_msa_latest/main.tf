resource "kubernetes_service" "this" {
  metadata {
    name      = local.metadata.name
    namespace = local.metadata.namespace
    labels    = local.metadata.labels
  }

  spec {
    dynamic "port" {
      for_each = local.spec.ports
      content {
        port        = port.value.port
        target_port = port.value.target_port
        protocol    = port.value.protocol
        name        = port.value.name
      }
    }

    selector = local.deployment_labels
    type     = "NodePort"
  }
}
