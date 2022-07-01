# Platform Mapping

## Characteristics

- [x] Category: Deployment
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-api-mapping

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
source | string | yes | - | mapping for source microservice (e.g. ftl-msa-kafka-in)
source_type | varchar(36) | yes | - | mapping for source type (e.g. message_in, message_out, entity_auth, entity_message; default: message_in)
content_type | string | no | - | mapping for content type (e.g. text/xml)
message_type | string | no | - | mapping for message type (e.g. pacs.008)
target | string | yes | - | mapping for target resource (e.g. topic-msg-in-pacs-008)

> NOTE: Unique constrain can be the combination of source, source_type, content_type, message_type, target, activated_at and deleted_at

## Examples

### Microservices Based Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.002 | ftl-msa-msg-pacs-002
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.008 | ftl-msa-msg-pacs-008
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.009 | ftl-msa-msg-pacs-009
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_out | text/xml | pacs.002 | ftl-msa-msg-out
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-002 | message_out | text/xml | pacs.002 | ftl-msa-msg-out
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-008 | message_out | text/xml | pacs.008 | ftl-msa-msg-out
378b2033-9b1d-409d-a4e6-eda7432c2a22 | 378b2033-9b1d-409d-a4e6-eda7432c2a22 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-008 | message_out | text/xml | pacs.002 | ftl-msa-msg-out
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-009 | message_out | text/xml | pacs.009 | ftl-msa-msg-out

### Internal Kafka Based Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
69f9a3cf-48fe-4804-9612-02fddd8d5dd7 | 69f9a3cf-48fe-4804-9612-02fddd8d5dd7 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.002 | ftl-msa-kafka-in
4838033c-e551-401e-85a6-5c6c2ca9a1a7 | 4838033c-e551-401e-85a6-5c6c2ca9a1a7 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.008 | ftl-msa-kafka-in
27ada4db-12f8-4271-9cfb-b577370d98f9 | 27ada4db-12f8-4271-9cfb-b577370d98f9 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.009 | ftl-msa-kafka-in
4f0be99b-7ce8-4bb3-9805-d69050d8a599 | 4f0be99b-7ce8-4bb3-9805-d69050d8a599 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_in | text/xml | pacs.002 | topic-msg-in-pacs-002
ed27b3d9-37bb-4c5e-967f-f8581658747a | ed27b3d9-37bb-4c5e-967f-f8581658747a | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_in | text/xml | pacs.008 | topic-msg-in-pacs-008
d9410185-4ca9-46fc-af6b-311ee97d1758 | d9410185-4ca9-46fc-af6b-311ee97d1758 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_in | text/xml | pacs.009 | topic-msg-in-pacs-009
7cebcd55-16fa-4106-a8c5-c1054cdc379f | 7cebcd55-16fa-4106-a8c5-c1054cdc379f | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_out | text/xml | pacs.002 | ftl-msa-kafka-in
7cebcd55-16fa-4106-a8c5-c1054cdc379f | 7cebcd55-16fa-4106-a8c5-c1054cdc379f | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_out | text/xml | pacs.002 | topic-msg-out-pacs-002
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_in | text/xml | pacs.002 | ftl-msa-msg-pacs-002
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_in | text/xml | pacs.008 | ftl-msa-msg-pacs-008
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_in | text/xml | pacs.009 | ftl-msa-msg-pacs-009
7d718acb-7abd-42fd-9674-1d9568c29ed0 | 7d718acb-7abd-42fd-9674-1d9568c29ed0 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-002 | message_out | text/xml | pacs.002 | ftl-msa-kafka-in
824f7cf2-c260-44a3-85e1-7ad0c53ddf00 | 824f7cf2-c260-44a3-85e1-7ad0c53ddf00 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-008 | message_out | text/xml | pacs.008 | ftl-msa-kafka-in
efda2a01-f507-4913-a7da-4fa7dd5d2fa2 | efda2a01-f507-4913-a7da-4fa7dd5d2fa2 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-009 | message_out | text/xml | pacs.009 | ftl-msa-kafka-in
44aeb344-0889-48e7-966d-eb1bbd81e14d | 44aeb344-0889-48e7-966d-eb1bbd81e14d | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_out | text/xml | pacs.002 | topic-msg-out-pacs-002
a697f8ed-197d-46ac-b86e-0fc3f26a6633 | a697f8ed-197d-46ac-b86e-0fc3f26a6633 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_out | text/xml | pacs.008 | topic-msg-out-pacs-008
b2a86d9b-24d3-486c-b6cd-0165b010d2ff | b2a86d9b-24d3-486c-b6cd-0165b010d2ff | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-in | message_out | text/xml | pacs.009 | topic-msg-out-pacs-009
4f0be99b-7ce8-4bb3-9805-d69050d8a599 | 4f0be99b-7ce8-4bb3-9805-d69050d8a599 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_out | text/xml | pacs.002 | ftl-msa-msg-out
ed27b3d9-37bb-4c5e-967f-f8581658747a | ed27b3d9-37bb-4c5e-967f-f8581658747a | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_out | text/xml | pacs.008 | ftl-msa-msg-out
d9410185-4ca9-46fc-af6b-311ee97d1758 | d9410185-4ca9-46fc-af6b-311ee97d1758 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-kafka-out | message_out | text/xml | pacs.009 | ftl-msa-msg-out

### External Sender RabbitMQ Based Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
d14abb20-8323-4fa5-a604-fa8308d36ef5 | d14abb20-8323-4fa5-a604-fa8308d36ef5 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | queue-custom-msg-out-pacs-008 | message_out | application/json | pacs.008 | ftl-msa-rmq-out
e1a2ee98-98ab-499c-b2e6-ebe56e5f4fa8 | e1a2ee98-98ab-499c-b2e6-ebe56e5f4fa8 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | queue-custom-msg-out-pacs-009 | message_out | application/json | pacs.009 | ftl-msa-rmq-out
9749cb3e-a575-4377-a380-015d14b2fc32 | 9749cb3e-a575-4377-a380-015d14b2fc32 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_out | application/json | pacs.008 | ftl-msa-msg-out
154a64c9-ba93-49d9-b8f2-f4c267a4c98b | 154a64c9-ba93-49d9-b8f2-f4c267a4c98b | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_out | application/json | pacs.009 | ftl-msa-msg-out
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-out | message_out | text/xml | pacs.008 | ftl-msa-msg-rmq-in
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-out | message_out | text/xml | pacs.009 | ftl-msa-msg-rmq-in
8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | 8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_out | text/xml | pacs.008 | queue-iso20022-msg-out-pacs-008
e85cb945-e330-437a-852f-c11ff8c01062 | e85cb945-e330-437a-852f-c11ff8c01062 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_out | text/xml | pacs.009 | queue-iso20022-msg-out-pacs-009

### External Intermediary RabbitMQ Based Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
bc402d80-49e7-4954-aae3-09adcfa3a8cf | bc402d80-49e7-4954-aae3-09adcfa3a8cf | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_in | text/xml | pacs.002 | ftl-msa-msg-in
9749cb3e-a575-4377-a380-015d14b2fc32 | 9749cb3e-a575-4377-a380-015d14b2fc32 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_in | text/xml | pacs.008 | ftl-msa-msg-in
154a64c9-ba93-49d9-b8f2-f4c267a4c98b | 154a64c9-ba93-49d9-b8f2-f4c267a4c98b | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_in | text/xml | pacs.009 | ftl-msa-msg-in
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.002 | ftl-msa-msg-pacs-002
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.008 | ftl-msa-msg-pacs-008
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | text/xml | pacs.009 | ftl-msa-msg-pacs-009
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_out | text/xml | pacs.002 | ftl-msa-msg-out
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-002 | message_out | text/xml | pacs.002 | ftl-msa-msg-out
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-008 | message_out | text/xml | pacs.008 | ftl-msa-msg-out
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-pacs-009 | message_out | text/xml | pacs.009 | ftl-msa-msg-out
7e17c2f8-ccb4-4896-9d90-e26ec8f805e7 | 7e17c2f8-ccb4-4896-9d90-e26ec8f805e7 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-out | message_out | text/xml | pacs.002 | ftl-msa-rmq-in
deda58f7-567e-4f68-99ae-3615039d748b | deda58f7-567e-4f68-99ae-3615039d748b | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-out | message_out | text/xml | pacs.008 | ftl-msa-rmq-in
43ca2bcb-964d-4ce3-8b48-242dca092bab | 43ca2bcb-964d-4ce3-8b48-242dca092bab | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-out | message_out | text/xml | pacs.009 | ftl-msa-rmq-in
a9c6e9c1-c4f6-4adc-ae1b-fc5180dc79d7 | a9c6e9c1-c4f6-4adc-ae1b-fc5180dc79d7 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_out | text/xml | pacs.002 | queue-iso20022-msg-out-pacs-002
8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | 8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_out | text/xml | pacs.008 | queue-iso20022-msg-out-pacs-008
e85cb945-e330-437a-852f-c11ff8c01062 | e85cb945-e330-437a-852f-c11ff8c01062 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_out | text/xml | pacs.009 | queue-iso20022-msg-out-pacs-009

### External Receiver RabbitMQ Based Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
7eee7dc1-5eae-4a92-a041-052454d5e4af | 7eee7dc1-5eae-4a92-a041-052454d5e4af | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | queue-iso20022-msg-in-pacs-002 | message_in | text/xml | pacs.002 | ftl-msa-rmq-out
d14abb20-8323-4fa5-a604-fa8308d36ef5 | d14abb20-8323-4fa5-a604-fa8308d36ef5 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | queue-iso20022-msg-in-pacs-008 | message_in | text/xml | pacs.008 | ftl-msa-rmq-out
bc402d80-49e7-4954-aae3-09adcfa3a8cf | bc402d80-49e7-4954-aae3-09adcfa3a8cf | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_in | text/xml | pacs.002 | ftl-msa-msg-in
9749cb3e-a575-4377-a380-015d14b2fc32 | 9749cb3e-a575-4377-a380-015d14b2fc32 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-out | message_in | text/xml | pacs.008 | ftl-msa-msg-in
9e4d66ef-c28f-4111-802c-f6104c8fcf15 | 9e4d66ef-c28f-4111-802c-f6104c8fcf15 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | application/json | pacs.002 | ftl-msa-msg-rmq-in
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-msg-in | message_in | application/json | pacs.008 | ftl-msa-msg-rmq-in
a9c6e9c1-c4f6-4adc-ae1b-fc5180dc79d7 | a9c6e9c1-c4f6-4adc-ae1b-fc5180dc79d7 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_in | application/json | pacs.002 | queue-custom-msg-in-pacs-002
8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | 8ff9d492-4aaa-4de1-ac31-89beed5b9c73 | null | 2022-02-07T17:56:07.937758-05:00 | 2f27a25b-b3aa-4190-924d-5aaf84850d12 | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-msa-rmq-in | message_in | application/json | pacs.008 | queue-custom-msg-in-pacs-008

### Authentication Based Entity Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-bofa-pub | entity_auth | null | null | bofa
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-citi-pub | entity_auth | null | null | citi
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-jpmc-pub | entity_auth | null | null | jpmc
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | e01964f6-e7c1-4adc-9d29-ebd695959969 | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-group-api-bofa-pub | entity_auth | null | null | bofa
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-citi-priv | entity_auth | null | null | citi
205d4f9c-6b42-4bd6-9609-8ba2d056d112 | 205d4f9c-6b42-4bd6-9609-8ba2d056d112 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-jpmc-priv | entity_auth | null | null | jpmc
f5733479-9287-48e9-ad25-41d1402c85fd | f5733479-9287-48e9-ad25-41d1402c85fd | e01964f6-e7c1-4adc-9d29-ebd695959969 | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-group-api-bofa-priv | entity_auth | null | null | bofa
8738b914-38d0-4a55-81f8-73cc05cf336b | 8738b914-38d0-4a55-81f8-73cc05cf336b | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-citi-mgr | entity_auth | null | null | citi
db5125ff-d0fb-47d6-aca6-ac2a912320f7 | db5125ff-d0fb-47d6-aca6-ac2a912320f7 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-jpmc-mgr | entity_auth | null | null | jpmc
783c9b6e-3f82-4dc4-a43c-486d2476f7ac | 783c9b6e-3f82-4dc4-a43c-486d2476f7ac | e01964f6-e7c1-4adc-9d29-ebd695959969 | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-group-api-bofa-mgr | entity_auth | null | null | bofa
adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-citi-bi | entity_auth | null | null | citi
5ebfa54c-60e4-453c-b320-345a978a1a8f | 5ebfa54c-60e4-453c-b320-345a978a1a8f | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | ftl-group-api-jpmc-bi | entity_auth | null | null | jpmc
3eecd65c-8405-4940-993e-01a32a7cd70b | 3eecd65c-8405-4940-993e-01a32a7cd70b | e01964f6-e7c1-4adc-9d29-ebd695959969 | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | ftl-group-api-bofa-bi | entity_auth | null | null | bofa

### Message Based Entity Mapping

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | source | source_type | content_type | message_type | target
---|--------------|----------|------------|------------|------------|------------|--------------|--------|-------------|-------------|--------------|-------
f572e270-f8bd-46d1-9aa5-e5542358c010 | f572e270-f8bd-46d1-9aa5-e5542358c010 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-08T17:56:07.937758-05:00 | 021000322 | entity_message | null | null | bofa
b26400f2-18eb-430c-9721-dc9e252fbdc5 | b26400f2-18eb-430c-9721-dc9e252fbdc5 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 021000089 | entity_message | null | null | citi
73bceff2-5ce5-4b9a-85d1-71d3e174f203 | 73bceff2-5ce5-4b9a-85d1-71d3e174f203 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 021100361 | entity_message | null | null | jpmc
