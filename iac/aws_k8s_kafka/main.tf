resource "kubectl_manifest" "this" {
  depends_on = [null_resource.this]

  count = length(data.kubectl_filename_list.this.matches)
  yaml_body = templatefile(element(data.kubectl_filename_list.this.matches, count.index),
    {
      EKS_NODE_GROUP = data.terraform_remote_state.aws_eks_node_group_kafka.outputs.node_group_name
    }
  )
}

resource "null_resource" "this" {
  triggers = {
    timestamp = timestamp()
  }

  provisioner "local-exec" {
    command = "/bin/bash helm.sh ${data.terraform_remote_state.aws_eks_cluster.outputs.cluster_name}"
  }
}
