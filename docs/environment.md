# Environment Variables

## Platform

- [ ] `FTL_CLOUD_PROVIDER` (e.g. aws, or google, or azurerm)
- [ ] `FTL_ACTIVE_REGION` (e.g. us-east-1)
- [ ] `FTL_PASSIVE_REGION` (e.g. us-east-2)
- [ ] `FTL_ACTIVE_VPC` (e.g. vpc-xxxxxxxx)
- [ ] `FTL_PASSIVE_VPC` (e.g. vpc-yyyyyyyy)
- [ ] `FTL_DOMAIN` (e.g. fintechless.com)
- [ ] `FTL_SUBDOMAIN_API` (e.g. api)
- [ ] `FTL_SUBDOMAIN_APP` (e.g. app)
- [ ] `FTL_SUBDOMAIN_AUTH` (e.g. auth)
- [ ] `FTL_FQDN_API` (e.g. api.fintechless.com; DO NOT EDIT)
- [ ] `FTL_FQDN_APP` (e.g. app.fintechless.com; DO NOT EDIT)
- [ ] `FTL_FQDN_AUTH` (e.g. auth.fintechless.com; DO NOT EDIT)
- [ ] `FTL_OWNER_FIRST_NAME` (e.g. John; DO NOT EDIT)
- [ ] `FTL_OWNER_LAST_NAME` (e.g. Smith; DO NOT EDIT)
- [ ] `FTL_OWNER_EMAIL` (e.g. john.smith@gmail.com; DO NOT EDIT)
- [ ] `FTL_ENVIRONMENT` (e.g. default)
- [ ] `FTL_RUNTIME_BUCKET` (e.g. ftl-api-runtime)
- [ ] `FTL_TFSTATE_BUCKET` (e.g. ftl-api-deploy)
- [ ] `FTL_TFSTATE_OBJECT` (e.g. terraform/fintechless/ftl-api/aws_eks_cluster/terraform.tfstate)
- [ ] `FTL_DB_HOST` (e.g. {name}.{unique_id}.{region}.rds.amazonaws.com)
- [ ] `FTL_DB_PORT` (e.g. 3306)
- [ ] `FTL_DB_USERNAME` (e.g. mysql_client)
- [ ] `FTL_DB_PASSWORD` (e.g. p@ssw0rd)
- [ ] `FTL_DB_ENGINE` (e.g. mysql)
- [ ] `FTL_DB_DATABASE` (e.g. ftl)
- [ ] `FTL_MSA_UUID_TTL` (e.g. 5; unit: seconds)
- [ ] `FTL_MSA_LATEST_LIMIT` (e.g. 50; unit: transaction ids)
- [ ] `FTL_MSA_MSG_PARSER_HOST` (e.g. https://www.iso20022.org/iso-20022-message-definitions)


## Client

### RabbitMQ

- [ ] `RABBITMQ_HOST` (e.g. b-{uuid}.mq.us-east-1.amazonaws.com)
- [ ] `RABBITMQ_PORT` (e.g. 5671)
- [ ] `RABBITMQ_USERNAME` (e.g. rmq_client)
- [ ] `RABBITMQ_PASSWORD` (e.g. p@ssw0rd)

### IBM MQ

- [ ] `IBMMQ_HOST` (e.g. b-{uuid}.mq.us-east-1.amazonaws.com)
- [ ] `IBMMQ_PORT` (e.g. 5671)
- [ ] `IBMMQ_USERNAME` (e.g. imq_client)
- [ ] `IBMMQ_PASSWORD` (e.g. p@ssw0rd)

### ActiveMQ

- [ ] `ACTIVEMQ_HOST` (e.g. b-{uuid}.mq.us-east-1.amazonaws.com)
- [ ] `ACTIVEMQ_PORT` (e.g. 5671)
- [ ] `ACTIVEMQ_USERNAME` (e.g. amq_client)
- [ ] `ACTIVEMQ_PASSWORD` (e.g. p@ssw0rd)

### FTP/SFTP

TBD

### HTTP/HTTPS

TBD


## AWS

### Amazon API Gateway

TBD

### Amazon Cognito

- [ ] `AWS_COGNITO_CLIENT_ID` (e.g. 1hfs8732vs1oh7pcnoa7234j88h)
- [ ] `AWS_COGNITO_CLIENT_SECRET` (e.g. b9gbijg6poksfgdfgddttkpjs4r1ssfgfdfj5b2lov9ig96vc3i)
- [ ] `AWS_COGNITO_USER_USERNAME` (e.g. cognito_username)
- [ ] `AWS_COGNITO_USER_PASSWORD` (e.g. p@ssw0rd)

### Amazon Kubernetes Service (EKS Fargate)

TBD

### Amazon Elastic Container Registry (ECR)

TBD

### AWS Secrets Manager

TBD

### Amazon Managed Grafana

TBD

### AWS IAM Roles & Policies

TBD

### Amazon VPC Endpoints

TBD

### Amazon S3

TBD

### Amazon DynamoDB

TBD

### Amazon Managed Streaming for Apache Kafka (MSK Serverless)

- [ ] `KAFKA_HOST` (e.g. b-0.{xxx}.{yyy}.{zzz}.kafka.us-east-1.amazonaws.com)
- [ ] `KAFKA_PORT` (e.g. 9092)
- [ ] `KAFKA_USERNAME` (e.g. kafka_client)
- [ ] `KAFKA_PASSWORD` (e.g. p@ssw0rd)

### Amazon Relational Database Service (RDS Serverless)

- [ ] `DB_HOST` (e.g. {name}.{unique_id}.us-east-1.rds.amazonaws.com)
- [ ] `DB_PORT` (e.g. 3306)
- [ ] `DB_USERNAME` (e.g. mysql_client)
- [ ] `DB_PASSWORD` (e.g. p@ssw0rd)

### Amazon ElastiCache (Redis)

TBD

### Amazon Simple Notification Service (SNS)

TBD

### Amazon Simple Queue Service (SQS)

TBD

### AWS CodeCommit

TBD

### AWS CodeBuild

TBD


## GCP

### Google Kubernetes Engine

TBD

### Container Registry

TBD

### Secrets Manager

TBD

### Grafana

TBD

### IAM Roles & Policies

TBD

### VPC Endpoints

TBD

### Cloud Storage

TBD

### Cloud Spanner

TBD

### Kafka

TBD

### Cloud SQL

TBD

### Memorystore (Redis)

TBD

### Pub/Sub

TBD

### Cloud Source Repositories

TBD

### Cloud Build

TBD
