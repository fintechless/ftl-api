# Message Category

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, regional, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-message-category

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
name | string | yes | - | message category name
description | string | no | - | message category description

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | name | description
---|--------------|----------|------------|------------|------------|------------|------|------------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | acmt | Account Management
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | admi | Administration
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | auth | Authorities
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | caaa | Acceptor to Acquirer Card Transactions
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | caad | Card Administration
205d4f9c-6b42-4bd6-9609-8ba2d056d112 | 205d4f9c-6b42-4bd6-9609-8ba2d056d112 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | caam | ATM Management
f5733479-9287-48e9-ad25-41d1402c85fd | f5733479-9287-48e9-ad25-41d1402c85fd | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | cafc | Fee collection
8738b914-38d0-4a55-81f8-73cc05cf336b | 8738b914-38d0-4a55-81f8-73cc05cf336b | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | cafm | Fraud Reporting and Disposition
db5125ff-d0fb-47d6-aca6-ac2a912320f7 | db5125ff-d0fb-47d6-aca6-ac2a912320f7 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | cain | Acquirer to Issuer Card Transactions
783c9b6e-3f82-4dc4-a43c-486d2476f7ac | 783c9b6e-3f82-4dc4-a43c-486d2476f7ac | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | camt | Cash Management
adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | canm | Network Management
5ebfa54c-60e4-453c-b320-345a978a1a8f | 5ebfa54c-60e4-453c-b320-345a978a1a8f | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | casp | Sale to POI Card Transactions
3eecd65c-8405-4940-993e-01a32a7cd70b | 3eecd65c-8405-4940-993e-01a32a7cd70b | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | casr | Settlement Reporting
5e0c8211-7e64-49a1-8e02-61e78ff314a4 | 5e0c8211-7e64-49a1-8e02-61e78ff314a4 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | catm | Terminal Management
abdc93cc-e281-440e-9f0e-2cfab61f92b4 | abdc93cc-e281-440e-9f0e-2cfab61f92b4 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | catp | ATM Card Transactions
156e4148-753f-4da4-bb97-180270d0cb79 | 156e4148-753f-4da4-bb97-180270d0cb79 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | colr | Collateral Management
87166175-61c2-4288-b3ed-7c8b02275131 | 87166175-61c2-4288-b3ed-7c8b02275131 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | fxtr | Foreign Exchange Trade
e4e0f778-86e3-46b8-9172-7aa8e2c3b23f | e4e0f778-86e3-46b8-9172-7aa8e2c3b23f | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | head | Business Application Header
b43e7d61-4b0a-4fc7-bb35-24ccbf44d79a | b43e7d61-4b0a-4fc7-bb35-24ccbf44d79a | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | pacs | Payments Clearing and Settlement
39cc4f8e-eb14-4f96-97e7-447e1db123f4 | 39cc4f8e-eb14-4f96-97e7-447e1db123f4 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | pain | Payments Initiation
7b48651e-ec86-4fc9-a99f-71bd6c8e2c4c | 7b48651e-ec86-4fc9-a99f-71bd6c8e2c4c | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | reda | Reference Data
d4d599a4-6e62-44cc-bdb6-61de3cf8e677 | d4d599a4-6e62-44cc-bdb6-61de3cf8e677 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | remt | Payments Remittance Advice
adc4451c-a83e-48d6-a6b3-83b0f6455498 | adc4451c-a83e-48d6-a6b3-83b0f6455498 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | secl | Securities Clearing
8a5c2ded-ae33-436c-b1a2-f8847113fb8d | 8a5c2ded-ae33-436c-b1a2-f8847113fb8d | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | seev | Securities Events
f0be1fea-fbc8-4c0d-892e-6e75edf971b3 | f0be1fea-fbc8-4c0d-892e-6e75edf971b3 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | semt | Securities Management
dee085d4-ecd8-420e-9221-038f6fa9dd46 | dee085d4-ecd8-420e-9221-038f6fa9dd46 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | sese | Securities Settlement
2ce5499e-f590-4de9-bcdf-c393a29b2792 | 2ce5499e-f590-4de9-bcdf-c393a29b2792 | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | setr | Securities Trade
4e7039a7-9de1-417c-b791-a6986818d1db | 4e7039a7-9de1-417c-b791-a6986818d1db | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | tsin | Trade Services Initiation
9397e5d2-e680-4ef4-a5f7-239125de84af | 9397e5d2-e680-4ef4-a5f7-239125de84af | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | tsmt | Trade Services Management
5892f861-8c4e-496c-8d3e-7feab5962ddc | 5892f861-8c4e-496c-8d3e-7feab5962ddc | null | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | tsrv | Trade Services
