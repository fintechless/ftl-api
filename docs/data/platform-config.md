# Platform Config

## Characteristics

- [x] Category: Deployment
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-api-config

## Definition

Name | Type | Required | Attributes | Details
-----|------|----------|------------|--------
id | varchar(36) | yes | primary | id, primary key using uuid function
reference_id | varchar(36) | yes | - | reference uuid, reference key for queries to filter our deleted records
child_id | varchar(36) | no | - | child uuid, reference key to new record that replaced deleted one
created_at | timestamp | yes | - | date and time when record was created (iso datetime with milliseconds and timezone)
created_by | varchar(36) | yes | - | member uuid who created the record (reference key to member table)
deleted_at | timestamp | no | - | date and time when record was deleted (iso datetime with milliseconds and timezone)
deleted_by | varchar(36) | no | - | member uuid who deleted the record (reference key to member table)
activated_at | timestamp | no | - | date and time when record became active (iso datetime with milliseconds and timezone)
var_key | string | yes | - | environment variable key (e.g. FTP_API_DOMAIN)
var_value | string | yes | - | environment variable value (e.g. api.fintechless.com)
ref_table | string | no | - | reference table (e.g. ftl-api-provider)
ref_key | string | no | - | reference key (e.g. 1)

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | var_key | var_value | ref_table | ref_key
---|--------------|----------|------------|------------|------------|------------|--------------|---------|-----------|-----------|--------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_DOMAIN | fintechless.com | - | -
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_SUBDOMAIN | api | - | -
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | FTL_CLOUD_PROVIDER | aws | - | -
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | FTL_ACTIVE_REGION | us-east-1 | - | -
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_PASSIVE_REGION | us-east-2 | - | -
205d4f9c-6b42-4bd6-9609-8ba2d056d112 | 205d4f9c-6b42-4bd6-9609-8ba2d056d112 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | FTL_ACTIVE_VPC | vpc-06ea98b6f846a781e | - | -
f5733479-9287-48e9-ad25-41d1402c85fd | f5733479-9287-48e9-ad25-41d1402c85fd | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_PASSIVE_VPC | vpc-009329bb164499676 | - | -
8738b914-38d0-4a55-81f8-73cc05cf336b | 8738b914-38d0-4a55-81f8-73cc05cf336b | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_MSA_UUID_TTL | 5 | - | -
db5125ff-d0fb-47d6-aca6-ac2a912320f7 | db5125ff-d0fb-47d6-aca6-ac2a912320f7 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | FTL_MSA_LATEST_LIMIT | 50 | - | -
5ebfa54c-60e4-453c-b320-345a978a1a8f | 5ebfa54c-60e4-453c-b320-345a978a1a8f | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | KAFKA_ENDPOINT | b-0.{xxx}.{yyy}.{zzz}.kafka.us-east-1.amazonaws.com | ftl-api-provider | e01964f6-e7c1-4adc-9d29-ebd695959969
3eecd65c-8405-4940-993e-01a32a7cd70b | 3eecd65c-8405-4940-993e-01a32a7cd70b | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | KAFKA_PORT | 9092 | ftl-api-provider | e01964f6-e7c1-4adc-9d29-ebd695959969
5e0c8211-7e64-49a1-8e02-61e78ff314a4 | 5e0c8211-7e64-49a1-8e02-61e78ff314a4 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | KAFKA_USERNAME | kafka_client | ftl-api-provider | e01964f6-e7c1-4adc-9d29-ebd695959969
abdc93cc-e281-440e-9f0e-2cfab61f92b4 | abdc93cc-e281-440e-9f0e-2cfab61f92b4 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | KAFKA_PASSWORD | p@ssw0rd | ftl-api-provider | e01964f6-e7c1-4adc-9d29-ebd695959969
156e4148-753f-4da4-bb97-180270d0cb79 | 156e4148-753f-4da4-bb97-180270d0cb79 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | RABBITMQ_ENDPOINT | b-{uuid}.mq.us-east-1.amazonaws.com | ftl-api-provider | 132a6d91-e978-4d71-8838-d82d730111ec
87166175-61c2-4288-b3ed-7c8b02275131 | 87166175-61c2-4288-b3ed-7c8b02275131 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | RABBITMQ_PORT | 9092 | ftl-api-provider | 132a6d91-e978-4d71-8838-d82d730111ec
e4e0f778-86e3-46b8-9172-7aa8e2c3b23f | e4e0f778-86e3-46b8-9172-7aa8e2c3b23f | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | RABBITMQ_USERNAME | rmq_client | ftl-api-provider | 132a6d91-e978-4d71-8838-d82d730111ec
b43e7d61-4b0a-4fc7-bb35-24ccbf44d79a | b43e7d61-4b0a-4fc7-bb35-24ccbf44d79a | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | RABBITMQ_PASSWORD | p@ssw0rd | ftl-api-provider | 132a6d91-e978-4d71-8838-d82d730111ec
