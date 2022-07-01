resource "aws_dynamodb_table" "this" {
  for_each = var.src

  name             = "${each.value.table_name}-${local.ftl_env}"
  hash_key         = each.value.hash_key
  range_key        = each.value.range_key
  billing_mode     = each.value.billing_mode
  stream_view_type = each.value.stream_view_type
  stream_enabled   = true

  dynamic "attribute" {
    for_each = each.value.attributes
    content {
      name = attribute.value.name
      type = attribute.value.type
    }
  }

  dynamic "global_secondary_index" {
    for_each = each.value.gsi_configs
    content {
      name               = global_secondary_index.value.name
      hash_key           = global_secondary_index.value.hash_key
      range_key          = global_secondary_index.value.range_key
      projection_type    = global_secondary_index.value.projection_type
      non_key_attributes = global_secondary_index.value.non_key_attributes
    }
  }

  point_in_time_recovery {
    enabled = false
  }

  tags = each.value.tags

  lifecycle {
    prevent_destroy = true
  }
}
