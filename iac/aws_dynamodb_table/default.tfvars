src = {
  "ftl-api-transaction" = {
    table_name       = "ftl-api-transaction"
    hash_key         = "id"
    range_key        = "created_at"
    billing_mode     = "PAY_PER_REQUEST"
    stream_view_type = "KEYS_ONLY"

    attributes = [
      {
        name = "id"
        type = "S"
      },
      {
        name = "transaction_id"
        type = "S"
      },
      {
        name = "status"
        type = "S"
      },
      {
        name = "created_at"
        type = "S"
      }
    ]

    gsi_configs = [
      {
        name               = "gsi-transactionid"
        hash_key           = "transaction_id"
        range_key          = "created_at"
        projection_type    = "INCLUDE"
        non_key_attributes = ["id", "created_at", "status"]
      },
      {
        name               = "gsi-status"
        hash_key           = "status"
        range_key          = "transaction_id"
        projection_type    = "INCLUDE"
        non_key_attributes = ["id", "transaction_id", "created_at"]
      }
    ]

    tags = {
      Description = "DynamoDB table for transactions"
    }
  },

  "ftl-api-liquidity" = {
    table_name       = "ftl-api-liquidity"
    hash_key         = "id"
    range_key        = "created_at"
    billing_mode     = "PAY_PER_REQUEST"
    stream_view_type = "KEYS_ONLY"

    attributes = [
      {
        name = "id"
        type = "S"
      },
      {
        name = "user_id"
        type = "S"
      },
      {
        name = "created_at"
        type = "S"
      },
      {
        name = "deployment_id"
        type = "S"
      },
    ]

    gsi_configs = [
      {
        name               = "gsi-userid-balance"
        hash_key           = "user_id"
        range_key          = "deployment_id"
        projection_type    = "ALL"
        non_key_attributes = []
      }
    ]

    tags = {
      Description = "DynamoDB table for liquidity"
    }
  }
}
