# Platform Microservice

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-microservice

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
name | varchar(100) | yes | - | "TBD"
description | text | no | - | "TBD"
active | boolean | no | - | "TBD"
path | text | no | - | "TBD"
runtime | varchar(100) | yes | - | "TBD"
code | text | no | - | "TBD"

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | name | description | active | path | runtime | code
---|--------------|----------|------------|------------|------------|------------|------|-------------|--------|------|---------|-----
8dd25286-bd45-4244-8f23-6c964c12e30d | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | Message In MSA | Incoming Messages MicroService: receives and validates ISO 20022 message, transforms into internal format and sends to corresponding processing workflow. | true | https://ftl-api-runtime-default-us-east-1-123456789012.s3.amazonaws.com/git/fintechless/ftl-msa-msg-in/main | python | "TBD"
