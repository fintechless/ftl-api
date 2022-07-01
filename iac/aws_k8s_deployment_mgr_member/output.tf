output "deployment_name" {
  value       = local.deployment_name
  description = "K8s deployment name."
}

output "port_name" {
  value       = local.deployment_name
  description = "The port used by the K8s deployment."
}

output "labels" {
  value       = local.metadata.labels
  description = "The labels attached to the K8s deployment."
}
