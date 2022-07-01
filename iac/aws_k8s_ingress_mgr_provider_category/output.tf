output "lb_dns_name" {
  value = kubernetes_ingress_v1.this.status[0].load_balancer[0].ingress[0].hostname
}

output "lb_port" {
  value = local.container_port
}

output "lb_health_check_path" {
  value = local.health_check_path
}

output "api_endpoint" {
  value = format(
    "http://%s:%s/mgr/provider_category",
    kubernetes_ingress_v1.this.status[0].load_balancer[0].ingress[0].hostname,
    local.container_port
  )
}

output "api_method" {
  value = "POST"
}
