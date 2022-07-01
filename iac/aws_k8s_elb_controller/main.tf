resource "kubectl_manifest" "this" {
  for_each  = data.kubectl_file_documents.this.manifests
  yaml_body = each.value
}
