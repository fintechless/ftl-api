resource "aws_lambda_permission" "this" {
  statement_id  = var.src.statement_id
  action        = var.src.action
  principal     = var.src.principal
  function_name = data.terraform_remote_state.aws_lambda_user_pool.outputs.name
  source_arn    = data.terraform_remote_state.aws_cognito_user_pool.outputs.arn
}
