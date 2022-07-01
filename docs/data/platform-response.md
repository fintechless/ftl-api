# Platform Response

## Characteristics

- [x] Category: Deployment
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-api-response

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
response_code | string | no | - | response code for each processed transactions
response_message | string | no | - | response message for each processed transactions
description | string | no | - | description of response code and response message

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | response_code | response_message | description
---|--------------|----------|------------|------------|------------|------------|---------------|------------------|------------
cde7ded6-f3b1-4cea-a36c-8baf095dd191 | cde7ded6-f3b1-4cea-a36c-8baf095dd191 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | HTTP200 | OK | The request processed successfully
fa3d89df-26a5-4fc6-a850-ea4eb520158c | fa3d89df-26a5-4fc6-a850-ea4eb520158c | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | HTTP201 | Created | The request succeeded, and a new resource was created as a result
dc564568-0e0f-4074-ba48-62cd472c0cf1 | dc564568-0e0f-4074-ba48-62cd472c0cf1 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | HTTP202 | Accepted | The request has been received, but not yet acted upon
839d2f20-2ba8-40d6-9948-674f313a8a8f | 839d2f20-2ba8-40d6-9948-674f313a8a8f | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS1 | INITIATED | New transaction was initiated
b0634d9a-75b8-4427-b74b-255a1108a968 | b0634d9a-75b8-4427-b74b-255a1108a968 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS2 | FAILED | Transaction processing failed
431a427f-15a5-4035-8fd0-dc869e81810a | 431a427f-15a5-4035-8fd0-dc869e81810a | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS3 | REJECTED | Transaction was rejected
9fc2349d-00b9-40bf-9b9a-11274ab55188 | 9fc2349d-00b9-40bf-9b9a-11274ab55188 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS4 | RECEIVED | Transaction was received
5558bd3a-4498-4904-9005-648e86b7c510 | 5558bd3a-4498-4904-9005-648e86b7c510 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS5 | PENDING | Transaction is pending for processing
c9a352cc-ce2e-4a7c-a049-1e81743ee86e | c9a352cc-ce2e-4a7c-a049-1e81743ee86e | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS6 | RELEASED | Transaction was released successfully
1edce29d-7d8a-49a0-8ab2-0163524dc3fa | 1edce29d-7d8a-49a0-8ab2-0163524dc3fa | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS7 | NOTIFIED | Transaction sender notified
b4ca2e58-ef86-4016-95e5-7c2a6968daa3 | b4ca2e58-ef86-4016-95e5-7c2a6968daa3 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | STATUS8 | CANCELED | Transaction was canceled
c990068c-ec62-4c69-84a1-7fe4def9b3ca | c990068c-ec62-4c69-84a1-7fe4def9b3ca | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | ACTC | ACTC | Payment initiated successfully
1c650c2f-40f5-4489-b99b-8d1b549e7fd0 | 1c650c2f-40f5-4489-b99b-8d1b549e7fd0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | ACSP | ACSP | Payment processed successfully
1336ab3d-8bee-4b54-8aee-aabc245ed349 | 1336ab3d-8bee-4b54-8aee-aabc245ed349 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | ACSC | ACSC | Payment released successfully
55dae0f9-9b16-4a6e-800c-638aea1d40f2 | 55dae0f9-9b16-4a6e-800c-638aea1d40f2 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | AC02 | RJCT | Debtor account number invalid or missing
d97dd1d9-02ed-4ee0-967d-dbbb5676c571 | d97dd1d9-02ed-4ee0-967d-dbbb5676c571 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | AC03 | RJCT | Creditor account number invalid or missing
d834ec97-e86b-40dc-8fa7-8aa4e690ed44 | d834ec97-e86b-40dc-8fa7-8aa4e690ed44 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | AC04 | RJCT | Account number specified has been closed on the bank of account's books
