output "cluster_name" {
  description = "EKS cluster name."
  value       = local.cluster_name
}

output "alb_name" {
  description = "EKS application load balancer name."
  value       = local.alb_name
}

output "created_at" {
  description = "Unix epoch timestamp in seconds for when the cluster was created."
  value       = aws_eks_cluster.this.created_at
}

output "k8s_endpoint" {
  description = "The endpoint for your Kubernetes API server."
  value       = aws_eks_cluster.this.endpoint
}

output "k8s_certificate" {
  description = "Nested attribute containing certificate-authority-data for your cluster."
  value       = aws_eks_cluster.this.certificate_authority[0].data
}

output "k8s_namespace" {
  description = "K8s namespace for shared environment."
  value       = var.src.k8s_namespace
}

output "k8s_version" {
  description = "K8s version for shared environment."
  value       = var.src.k8s_version
}

output "k8s_port" {
  description = "K8s port for shared environment."
  value       = var.src.k8s_port
}

output "oidc_issuer" {
  description = "OpenID Connect Issuer"
  value       = aws_eks_cluster.this.identity[0].oidc[0].issuer
}

output "role_name" {
  description = "IAM role name."
  value       = data.terraform_remote_state.aws_iam_eks.outputs.name
}

output "vpc_id" {
  description = "Current VPC ID."
  value       = data.terraform_remote_state.aws_sg_eks.outputs.vpc_id
}

output "subnet_ids" {
  description = "List of subnet IDs."
  value       = tolist(aws_eks_cluster.this.vpc_config[0].subnet_ids)
}

output "security_group_ids" {
  description = "List of security group IDs."
  value = concat(
    tolist(aws_eks_cluster.this.vpc_config[0].security_group_ids),
    [aws_eks_cluster.this.vpc_config[0].cluster_security_group_id]
  )
}
