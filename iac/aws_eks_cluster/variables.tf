variable "src" {
  type = object({
    backend        = string
    config_key_iam = string
    config_key_sgr = string
    cluster_name   = string
    alb_name       = string
    k8s_namespace  = string
    k8s_version    = string
    k8s_port       = number
  })
}
