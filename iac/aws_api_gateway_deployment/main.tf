resource "aws_api_gateway_deployment" "this" {
  rest_api_id       = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  description       = var.src.description
  stage_description = var.src.stage_description

  triggers = {
    # redeployment = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.body_hash
    redeployment = timestamp()
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_api_gateway_stage" "this" {
  deployment_id = aws_api_gateway_deployment.this.id
  rest_api_id   = data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id
  stage_name    = var.src.stage_name

  access_log_settings {
    destination_arn = aws_cloudwatch_log_group.this.arn
    format = jsonencode(
      {
        caller         = "$context.identity.caller"
        httpMethod     = "$context.httpMethod"
        ip             = "$context.identity.sourceIp"
        protocol       = "$context.protocol"
        requestId      = "$context.requestId"
        requestTime    = "$context.requestTime"
        resourcePath   = "$context.resourcePath"
        responseLength = "$context.responseLength"
        status         = "$context.status"
        user           = "$context.identity.user"
      }
    )
  }
}

resource "aws_cloudwatch_log_group" "this" {
  name              = format("%s_%s/%s", var.src.name_prefix, data.terraform_remote_state.aws_api_gateway_rest_api.outputs.id, var.src.stage_name)
  retention_in_days = tonumber(var.src.retention_in_days)
}

resource "aws_secretsmanager_secret_version" "this" {
  depends_on = [aws_api_gateway_stage.this]
  secret_id  = data.aws_secretsmanager_secret.this.id
  secret_string = jsonencode(merge(local.ftl_cicd_secret_map, {
    FTL_FQDN_API = local.ftl_domain == "" ? aws_api_gateway_stage.this.invoke_url : format("%s.%s", local.ftl_env == "default" ? local.ftl_subdomain_api : "${local.ftl_subdomain_api}-${local.ftl_env}", local.ftl_domain)
  }))
}
