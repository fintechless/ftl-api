resource "aws_iam_openid_connect_provider" "this" {
  client_id_list  = ["sts.amazonaws.com"]
  thumbprint_list = [data.tls_certificate.this.certificates[0].sha1_fingerprint]
  url             = data.terraform_remote_state.aws_eks_cluster.outputs.oidc_issuer
}

resource "aws_iam_role" "this" {
  count       = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name        = "${var.src.role_name}-${local.ftl_env}"
  description = var.src.description

  assume_role_policy = templatefile("${path.module}/template/assume_policy.json.tpl",
    {
      iam_openid_connect_provider_arn = aws_iam_openid_connect_provider.this.arn
      oidc_issuer_sub                 = local.oidc_issuer_sub
      oidc_issuer_aud                 = local.oidc_issuer_aud
    }
  )
}

resource "aws_iam_policy" "this" {
  count  = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  name   = "${var.src.policy_name}-${local.ftl_env}"
  path   = var.src.path
  policy = file("${path.module}/template/trust_policy.json.tpl")
}

resource "aws_iam_role_policy_attachment" "this" {
  count      = (data.aws_region.this.name == local.ftl_active) ? 1 : 0
  policy_arn = aws_iam_policy.this[0].arn
  role       = aws_iam_role.this[0].name
}
