resource "kubectl_manifest" "this" {
  depends_on = [kubernetes_namespace.this]

  yaml_body = templatefile("template/aws_auth_configmap.yaml.tpl",
    {
      account_id = data.aws_caller_identity.this.account_id
      role_names = concat(
        [for name in data.aws_iam_roles.this.names : name],
        [data.terraform_remote_state.aws_eks_cluster.outputs.role_name],
      )
      sso_users = [
        "AWSReservedSSO_AWSAdministratorAccess_9297a600de88b7a6",
        "ServiceRoleForCicdPipelines"
      ]
    }
  )
}

resource "kubernetes_namespace" "this" {
  metadata {
    name = local.k8s.namespace
  }
}
