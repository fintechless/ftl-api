data "kubectl_filename_list" "this" {
  pattern = "${path.module}/template/*.yaml.tpl"
}

data "terraform_remote_state" "aws_eks_node_group_kafka" {
  backend = var.src.backend
  config  = try(local.config, {})
}
