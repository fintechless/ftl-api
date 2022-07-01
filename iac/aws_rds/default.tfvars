src = {
  backend                             = "s3"
  config_key_rds_subnet_group         = "terraform/fintechless/ftl-api/aws_rds_subnet_group/terraform.tfstate"
  config_key_eks_cluster              = "terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate"
  allocated_storage                   = 1
  backtrack_window                    = 0
  backup_retention_period             = 1
  cluster_identifier                  = "ftl-aurora-mysql"
  database_name                       = "ftl"
  db_cluster_parameter_group_name     = "default.aurora-mysql8.0"
  deletion_protection                 = false
  enabled_cloudwatch_logs_exports     = []
  engine                              = "aurora-mysql"
  engine_version                      = "8.0.mysql_aurora.3.02.0"
  iam_database_authentication_enabled = false
  iam_roles                           = []
  iops                                = 0
  master_username                     = "admin"
  port                                = 3306
  preferred_backup_window             = "08:54-09:24"
  preferred_maintenance_window        = "mon:08:04-mon:08:34"
  skip_final_snapshot                 = true
  storage_encrypted                   = false
  serverlessv2_scaling_configuration = {
    max_capacity = 16
    min_capacity = 2
  }
}

tags = {
  Description = "AWS RDS"
}
