resource "aws_cognito_user_group" "this" {
  for_each     = { for ug in var.src.user_groups : ug.name => ug }
  name         = "${each.value.name}-${local.ftl_env}"
  description  = each.value.description
  user_pool_id = data.terraform_remote_state.aws_cognito_user_pool.outputs.id
}
