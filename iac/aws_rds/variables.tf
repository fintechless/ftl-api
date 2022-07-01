variable "src" {
  type = object({
    backend                             = string
    config_key_rds_subnet_group         = string
    config_key_eks_cluster              = string
    allocated_storage                   = number
    backtrack_window                    = number
    backup_retention_period             = number
    cluster_identifier                  = string
    database_name                       = string
    db_cluster_parameter_group_name     = string
    deletion_protection                 = bool
    enabled_cloudwatch_logs_exports     = list(string)
    engine                              = string
    engine_version                      = string
    iam_database_authentication_enabled = bool
    iam_roles                           = list(string)
    iops                                = number
    master_username                     = string
    port                                = number
    preferred_backup_window             = string
    preferred_maintenance_window        = string
    skip_final_snapshot                 = bool
    storage_encrypted                   = bool
    serverlessv2_scaling_configuration = object({
      max_capacity = number
      min_capacity = number
    })
  })
}

variable "tags" {
  type = object({
    Description = string
  })
}
