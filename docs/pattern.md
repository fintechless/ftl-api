# Patterns and Conventions

## Identity Group Name

- [ ] ftl-group-web-admin => scope: all
- [ ] ftl-group-api-admin => scope: all
- [ ] ftl-group-api-mgr => scope: public, private && mgr
- [ ] ftl-group-api-bi => scope: public, private && bi
- [ ] ftl-group-api-user => scope: public
- [ ] ftl-group-api-{entity}-pub => scope: public
- [ ] ftl-group-api-{entity}-priv => scope: public && private
- [ ] ftl-group-api-{entity}-mgr => scope: public, private && mgr
- [ ] ftl-group-api-{entity}-bi => scope: public, private && bi

## Storage Bucket Name

### Management (Active Region)

- [ ] ftl-api-mgr-default-{active_region}-{account}
- [ ] ftl-api-mgr-dev-{active_region}-{account}
- [ ] ftl-api-mgr-test-{active_region}-{account}
- [ ] ftl-api-mgr-stage-{active_region}-{account}

### Management (Passive Region)

- [ ] ftl-api-mgr-default-{passive_region}-{account}
- [ ] ftl-api-mgr-dev-{passive_region}-{account}
- [ ] ftl-api-mgr-test-{passive_region}-{account}
- [ ] ftl-api-mgr-stage-{passive_region}-{account}

### Deployment (Active Region)

- [ ] ftl-api-deploy-default-{active_region}-{account}
- [ ] ftl-api-deploy-dev-{active_region}-{account}
- [ ] ftl-api-deploy-test-{active_region}-{account}
- [ ] ftl-api-deploy-stage-{active_region}-{account}

### Deployment (Passive Region)

- [ ] ftl-api-deploy-default-{passive_region}-{account}
- [ ] ftl-api-deploy-dev-{passive_region}-{account}
- [ ] ftl-api-deploy-test-{passive_region}-{account}
- [ ] ftl-api-deploy-stage-{passive_region}-{account}

### Runtime (Active Region)

- [ ] ftl-api-runtime-default-{active_region}-{account}
- [ ] ftl-api-runtime-dev-{active_region}-{account}
- [ ] ftl-api-runtime-test-{active_region}-{account}
- [ ] ftl-api-runtime-stage-{active_region}-{account}

### Runtime (Passive Region)

- [ ] ftl-api-runtime-default-{passive_region}-{account}
- [ ] ftl-api-runtime-dev-{passive_region}-{account}
- [ ] ftl-api-runtime-test-{passive_region}-{account}
- [ ] ftl-api-runtime-stage-{passive_region}-{account}

## Storage Object Path

### Management

- [ ] ftl-api-mgr-default-{region}-{account}/404.html
- [ ] ftl-api-mgr-default-{region}-{account}/favicon.ico
- [ ] ftl-api-mgr-default-{region}-{account}/index.html

### Deployment

- [ ] ftl-api-deploy-default-{region}-{account}/schema/category.json
- [ ] ftl-api-deploy-default-{region}-{account}/schema/xsd/{iso20022_message_id}.xsd
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-api/{environment}/{lambda_function}/lambda_function.txt
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-api/{environment}/{lambda_function}/lambda_function.zip
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-mgr/{environment}/.env
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-mgr/{environment}/index.txt
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-msa-{msa_name}/{environment}/{lambda_function}/lambda_function.txt
- [ ] ftl-api-deploy-default-{region}-{account}/deploy/fintechless/ftl-msa-{msa_name}/{environment}/{lambda_function}/lambda_function.zip
- [ ] ftl-api-deploy-default-{region}-{account}/terraform/fintechless/ftl-api/{terrahub_component}/terraform.tfstate
- [ ] ftl-api-deploy-default-{region}-{account}/terraform/fintechless/ftl-mgr/{terrahub_component}/terraform.tfstate
- [ ] ftl-api-deploy-default-{region}-{account}/terraform_workspaces/{environment}/terraform/fintechless/ftl-api/{terrahub_component}/terraform.tfstate
- [ ] ftl-api-deploy-default-{region}-{account}/terraform_workspaces/{environment}/terraform/fintechless/ftl-mgr/{terrahub_component}/terraform.tfstate
- [ ] ftl-api-deploy-default-{region}-{account}/terraform/fintechless/ftl-msa-{msa_name}/{terrahub_component}/terraform.tfstate
- [ ] ftl-api-deploy-default-{region}-{account}/terraform_workspaces/{environment}/terraform/fintechless/ftl-msa-{msa_name}/{terrahub_component}/terraform.tfstate

### Runtime

- [ ] ftl-api-runtime-default-{region}-{account}/git/fintechless/ftl-msa-{msa_name}/{branch}/Dockerfile
- [ ] ftl-api-runtime-default-{region}-{account}/in/{yyyy}/{mm}/{dd}/{hh}/{ii}/{ss}/{ms_by_hundreds}{if_not_gmt_then_timezone_as_digits}/{uuid}-{message_type}.xml
- [ ] ftl-api-runtime-default-{region}-{account}/out/{yyyy}/{mm}/{dd}/{hh}/{ii}/{ss}/{ms_by_hundreds}{if_not_gmt_then_timezone_as_digits}/{uuid}-{message_type}.xml
- [ ] ftl-api-runtime-default-{region}-{account}/liquidity/{yyyy}/{mm}/{dd}/{hh}/{ii}/{ss}/{records_one_per_line}.json
- [ ] ftl-api-runtime-default-{region}-{account}/transaction/{yyyy}/{mm}/{dd}/{hh}/{ii}/{ss}/{records_one_per_line}.json
