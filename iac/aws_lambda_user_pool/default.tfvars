src = {
  backend    = "s3"
  config_key = "terraform/fintechless/ftl-api/aws_iam_lambda_user_pool/terraform.tfstate"

  function_name = "ftl-api-token-generator"
  description   = "Lambda function for token generation"
  handler       = "lambda_function.handler"
  runtime       = "nodejs14.x"
  s3_path       = "deploy/fintechless/ftl-api/dev/aws_lambda_user_pool"
  s3_file       = "lambda_function.zip"
  retention     = "14"
}
