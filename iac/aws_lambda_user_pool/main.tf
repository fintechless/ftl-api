resource "aws_lambda_function" "this" {
  function_name    = "${var.src.function_name}-${local.ftl_env}"
  description      = var.src.description
  handler          = var.src.handler
  runtime          = var.src.runtime
  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256("lambda_function.zip")
  # s3_bucket        = local.ftl_bucket
  # s3_key           = format("%s/%s", var.src.s3_path, var.src.s3_file)
  # source_code_hash = filebase64sha256(var.src.s3_file)
  role = data.terraform_remote_state.aws_iam_lambda_user_pool.outputs.arn

  tags = {
    Name = "${var.src.function_name}-${local.ftl_env}"
  }
}

resource "aws_cloudwatch_log_group" "this" {
  name              = "/aws/lambda/${aws_lambda_function.this.function_name}"
  retention_in_days = tonumber(var.src.retention)
}
