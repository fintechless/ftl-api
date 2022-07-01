data "kubectl_file_documents" "this" {
  content = templatefile("${path.module}/template/aws-load-balancer-controller.yaml.tpl",
    {
      CLUSTER_NAME = data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name
      IAM_ROLE_ARN = data.terraform_remote_state.aws_iam_eks_elb.outputs.arn
    }
  )
}

data "terraform_remote_state" "aws_iam_eks_elb" {
  backend = var.src.backend
  config  = try(local.config, {})
}
