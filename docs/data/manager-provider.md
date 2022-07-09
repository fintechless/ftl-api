# Provider

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-provider

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
active | boolean | no | - | "TBD"
activated_at | timestamp | no | - | date and time when record became active (iso datetime with milliseconds and timezone)
name | string | yes | - | name of provider instance (e.g. Shared Kafka or Shared Kafka DEV)
description | string | yes | - | description of provider instance
secret_ref | string | no | - | secrets manager reference keyword

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | active | activated_at | name | description | secret_ref
---|--------------|----------|------------|------------|------------|------------|--------|--------------|------|-------------|----------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared Kafka | Shared Kafka Services - Production | FTL_SECRET_KAFKA_DEFAULT_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared Kafka DEV | Shared Kafka Services - Development | FTL_SECRET_KAFKA_DEV_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared Kafka TEST | Shared Kafka Services - Testing | FTL_SECRET_KAFKA_TEST_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared Kafka STAGE | Shared Kafka Services - Staging | FTL_SECRET_KAFKA_STAGE_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared RabbitMQ | Shared RabbitMQ Services - Production | FTL_SECRET_RABBITMQ_DEFAULT_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
205d4f9c-6b42-4bd6-9609-8ba2d056d112 | 205d4f9c-6b42-4bd6-9609-8ba2d056d112 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared RabbitMQ DEV | Shared RabbitMQ Services - Development | FTL_SECRET_RABBITMQ_DEV_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
f5733479-9287-48e9-ad25-41d1402c85fd | f5733479-9287-48e9-ad25-41d1402c85fd | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared RabbitMQ TEST | Shared RabbitMQ Services - Testing | FTL_SECRET_RABBITMQ_TEST_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
8738b914-38d0-4a55-81f8-73cc05cf336b | 8738b914-38d0-4a55-81f8-73cc05cf336b | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | false | 2022-02-07T17:56:07.937758-05:00 | Shared RabbitMQ STAGE | Shared RabbitMQ Services - Staging | FTL_SECRET_RABBITMQ_STAGE_d850752f-ec4e-3df6-bcab-2dcb376b8ab1
