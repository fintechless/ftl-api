# Transaction

## Characteristics

- [x] Category: Runtime
- [x] Requirements: global, immutable, not cachable, low latency
- [x] Source: nosql
- [x] Identifier: ftl-api-transation

## Definition

Name | Type | Required | Attributes | Details
-----|------|----------|------------|--------
id | string | yes | unique key | uuid, id for each record in current table
created_at | timestamp | yes | - | date and time when record was created (iso datetime with milliseconds and timezone)
request_id | string | - | uuid, request_id for each api request / response
requested_at | timestamp | yes | - | date and time when request was received (iso datetime with milliseconds and timezone)
transaction_id | string | yes | global secondary index | uuid, transaction_id for each api response
status | string | yes | global secondary index | predefined value from a list of statuses
message_type | string | no | - | message type retrieved from the actual xml
response_code | string | no | - | response code for each processed transactions
response_message | string | no | - | response message for each processed transactions
currency | string | no | - | currency used for liquidity (e.g. USD or EUR)
amount | float | no | - | current amount to add or remove from liquidity balance
retrieved_at | timestamp | no | - | date and time when record was retrieved (iso datetime with milliseconds and timezone)
storage_path | string | no | - | path in storage bucket where original message is archived

## Examples

```json
[
  {
    "id": "bea07510-92fe-4b8a-9fcb-145ae15e79a6",
    "created_at": "2022-02-07T17:56:07.937758-05:00",
    "request_id": "a4ad78f7-57ce-4103-99c2-22017f0c1d80",
    "requested_at": "2022-02-07T17:56:07.758377-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "INITIATED"
  },
  {
    "id": "118d8255-d0f3-4538-a592-fbd94cc9171b",
    "created_at": "2022-02-07T17:56:08.519859-05:00",
    "request_id": "a35637fc-80a8-4425-8c12-6fdb937542cc",
    "requested_at": "2022-02-07T17:56:08.290054-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "RECEIVED",
    "message_type": "pacs.008.001.10",
    "response_code": "HTTP201",
    "response_message": "Created",
    "storage_path": "in/2022/02/07/17/56/08/200-0500/6d3f0c95-8f0d-41c8-989b-2992036a256a-pacs.008.001.10.xml"
  },
  {
    "id": "4ce63858-4842-4dea-8ebc-18bc5f29769a",
    "created_at": "2022-02-07T17:56:08.544367-05:00",
    "request_id": "ef2e88a6-26b2-4f35-b0d5-883c4f452da9",
    "requested_at": "2022-02-07T17:56:08.290054-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "NOTIFIED",
    "message_type": "pacs.002.001.12",
    "response_code": "HTTP200",
    "response_message": "OK",
    "retrieved_at": "2022-02-07T17:56:56.316669-05:00",
    "storage_path": "out/2022/02/07/17/56/08/200-0500/6d3f0c95-8f0d-41c8-989b-2992036a256a-pacs.002.001.12.xml"
  },
  {
    "id": "15ec00d7-0f5b-4254-9e41-be40158ee031",
    "created_at": "2022-02-07T17:56:08.792694-05:00",
    "request_id": "df23d7d9-4011-46b3-a528-ecaba63811e1",
    "requested_at": "2022-02-07T17:56:08.290054-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "requested_at": "2022-02-07T17:56:08.378246-05:00",
    "status": "PENDING",
    "response_code": "ACTC",
    "response_message": "PENDING",
    "currency": "USD",
    "amount": 100
  },
  {
    "id": "accdc108-5610-484d-83d9-ac0f82825926",
    "created_at": "2022-02-07T17:56:08.941770-05:00",
    "request_id": "6628e068-17d7-421e-b9bc-e5ecb8f5f4c2",
    "requested_at": "2022-02-07T17:56:07.857094-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "RELEASED",
    "message_type": "pacs.008.001.10",
    "response_code": "ACTC",
    "response_message": "RELEASED",
    "currency": "USD",
    "amount": 100,
    "retrieved_at": "2022-02-07T17:56:56.896157-05:00",
    "storage_path": "out/2022/02/07/17/56/07/800-0500/6d3f0c95-8f0d-41c8-989b-2992036a256a-pacs.008.001.10.xml"
  },
  {
    "id": "1148ce50-e5b3-4e27-9129-a07ee63d5d4b",
    "created_at": "2022-02-07T17:56:09.561934-05:00",
    "request_id": "9b06f37e-42a4-4a67-9285-58e444db0b92",
    "requested_at": "2022-02-07T17:56:09.003239-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "NOTIFIED",
    "message_type": "pacs.002.001.12",
    "response_code": "HTTP200",
    "response_message": "OK",
    "retrieved_at": "2022-02-07T17:56:57.433999-05:00",
    "storage_path": "out/2022/02/07/17/56/09/0-0500/6d3f0c95-8f0d-41c8-989b-2992036a256a-pacs.002.001.12.xml"
  },
  {
    "id": "11d9c33f-b546-4521-bb56-af9f8fb65a13",
    "created_at": "2022-02-07T17:56:56.316669-05:00",
    "request_id": "50a9e1b3-5de2-4970-a01d-19c50d74fa34",
    "requested_at": "2022-02-07T17:56:56.316669-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "RETRIEVED"
  },
  {
    "id": "e0c1e5ac-4957-4dc0-880c-c65354e74a3f",
    "created_at": "2022-02-07T17:56:56.896157-05:00",
    "request_id": "18827020-e2a7-4296-ac3a-b2520a4d3795",
    "requested_at": "2022-02-07T17:56:56.896157-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "RETRIEVED"
  },
  {
    "id": "0f72906d-30ab-4443-9a0f-ca13f01ce312",
    "created_at": "2022-02-07T17:56:57.433999-05:00",
    "request_id": "2a25439b-80d2-4a4e-9653-f11a49fe0c63",
    "requested_at": "2022-02-07T17:56:57.433999-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "status": "RETRIEVED"
  }
]
```
