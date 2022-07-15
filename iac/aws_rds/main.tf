resource "random_password" "this" {
  length           = 16
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

resource "aws_rds_cluster" "this" {
  backtrack_window                    = var.src.backtrack_window
  backup_retention_period             = var.src.backup_retention_period
  cluster_identifier                  = var.src.cluster_identifier
  engine                              = var.src.engine
  engine_version                      = var.src.engine_version
  enabled_cloudwatch_logs_exports     = var.src.enabled_cloudwatch_logs_exports
  iam_database_authentication_enabled = var.src.iam_database_authentication_enabled
  iam_roles                           = var.src.iam_roles
  # iops                                = var.src.iops
  availability_zones                  = data.terraform_remote_state.aws_rds_subnet_group.outputs.availability_zones
  database_name                       = var.src.database_name
  deletion_protection                 = var.src.deletion_protection
  master_username                     = var.src.master_username
  master_password                     = random_password.this.result
  preferred_backup_window             = var.src.preferred_backup_window
  preferred_maintenance_window        = var.src.preferred_maintenance_window
  skip_final_snapshot                 = var.src.skip_final_snapshot
  storage_encrypted                   = var.src.storage_encrypted
  vpc_security_group_ids              = data.terraform_remote_state.aws_eks_cluster.outputs.security_group_ids
  tags                                = var.tags

  serverlessv2_scaling_configuration {
    min_capacity = var.src.serverlessv2_scaling_configuration.min_capacity
    max_capacity = var.src.serverlessv2_scaling_configuration.max_capacity
  }
}

resource "aws_secretsmanager_secret_version" "this" {
  depends_on = [aws_rds_cluster.this]
  secret_id  = data.aws_secretsmanager_secret.this.id
  secret_string = jsonencode(merge(local.ftl_cicd_secret_map, {
    FTL_DB_USERNAME = aws_rds_cluster.this.master_username
    FTL_DB_ENGINE   = aws_rds_cluster.this.engine
    FTL_DB_HOST     = aws_rds_cluster.this.endpoint
    FTL_DB_PORT     = aws_rds_cluster.this.port
    FTL_DB_DATABASE = aws_rds_cluster.this.database_name
    FTL_DB_PASSWORD = random_password.this.result
  }))
}
