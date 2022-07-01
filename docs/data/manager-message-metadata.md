# Message Metadata

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, regional, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-message-metadata

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
unique_key | string | yes | - | message id as definied by iso 20022 (e.g. pacs.008.001.10)
category_id | varchar(36) | yes | - | category uuid, foreign key to message category table
mapping | string | yes | - | message unique identifier for mapping table (e.g. pacs.008)
description | string | no | - | message description as defined by iso 20022
storage_path | string | no | - | path in storage bucket where message schema is stored

> NOTE: Unique constrain can be the combination of unique_key, activated_at and deprecated_at

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | unique_key | category_id | mapping | description | storage_path
---|--------------|----------|------------|------------|------------|------------|--------------|------------|-------------|---------|------------|-------------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | pacs.002.001.12 | 119 | pacs.002 | FI To FI Payment Status Report V12 | schema/xsd/pacs.002.001.12.xsd
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | pacs.008.001.10 | 119 | pacs.008 | FI To FI Customer Credit Transfer V10 | schema/xsd/pacs.008.001.10.xsd
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | pacs.009.001.10 | 119 | pacs.009 | Financial Institution Credit Transfer V10 | schema/xsd/pacs.009.001.10.xsd
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | pain.013.001.09 | 120 | pain.013 | Creditor Payment Activation Request V09 | schema/xsd/pain.013.001.09.xsd
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | 2022-02-07T17:56:07.937758-05:00 | pain.014.001.09 | 120 | pain.014 | Creditor Payment Activation Request Status Report V09 | schema/xsd/pain.014.001.09.xsd
