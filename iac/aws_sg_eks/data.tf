data "aws_vpc" "this" {
  id = local.ftl_vpc[data.aws_region.this.name]
}
