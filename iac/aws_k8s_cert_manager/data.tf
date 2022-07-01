data "kubectl_file_documents" "this" {
  content = file("${path.module}/template/cert-manager.yaml")
}
