resource "kubectl_manifest" "this" {
  depends_on = [kubernetes_namespace.this]

  for_each  = data.kubectl_file_documents.this.manifests
  yaml_body = each.value
}

resource "kubernetes_namespace" "this" {
  metadata {
    name = "cert-manager"
  }
}
