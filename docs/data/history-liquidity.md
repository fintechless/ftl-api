# Liquidity

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, immutable, cachable, worm
- [x] Source: storage
- [x] Identifier: ftl-api-runtime-{environment}-{region}-{account}/liquidity/{yyyy}/{mm}/{dd}/{hh}/{ii}/{ss}/{records_one_per_line}.json

## Definition

Name | Type | Required | Attributes | Details
-----|------|----------|------------|--------
id | string | yes | unique key | uuid, id for each record in current table
created_at | timestamp | yes | - | date and time when record was created (iso datetime with milliseconds and timezone)
request_id | string | - | uuid, request_id for each api request / response
requested_at | timestamp | yes | - | date and time when request was received (iso datetime with milliseconds and timezone)
transaction_id | string | yes | global secondary index | uuid, transaction_id for each api response
entity_id | string | yes | global secondary index | entity identifier to uniquely reference the liquidity owner
currency | string | yes | - | currency used for liquidity (e.g. USD or EUR)
amount | float | yes | - | current amount to add or remove from liquidity balance
balance | float | yes | - | current liquidity balance

## Examples

```json
[
  {
    "id": "fa0cadc8-dfdd-4411-8ac0-75a47e876178",
    "created_at": "2022-02-07T17:56:07.937758-05:00",
    "request_id": "8dae600e-5276-4c1a-b31f-cd7c98430702",
    "requested_at": "2022-02-07T17:56:07.758377-05:00",
    "transaction_id": "6d3f0c95-8f0d-41c8-989b-2992036a256a",
    "entity_id": "bank_of_america",
    "currency": "USD",
    "amount": 100.00,
    "balance": 100.00
  },
  {
    "id": "16d64f21-4533-4217-a5fc-8e2e9057844b",
    "created_at": "2022-02-07T17:56:08.937758-05:00",
    "request_id": "c3a0d52d-1032-4ef6-bc43-3811ff33c479",
    "requested_at": "2022-02-07T17:56:08.758377-05:00",
    "transaction_id": "7d3f0c95-8f0d-41c8-989b-2992036a256b",
    "entity_id": "bank_of_america",
    "currency": "USD",
    "amount": -50.00,
    "balance": 50.00
  },
  {
    "id": "cf320787-7cde-496d-ba28-a917811fd907",
    "created_at": "2022-02-07T17:56:09.937758-05:00",
    "request_id": "38a80dbb-af36-4508-8e7e-f4a41aa7cd2a",
    "requested_at": "2022-02-07T17:56:09.758377-05:00",
    "transaction_id": "8d3f0c95-8f0d-41c8-989b-2992036a256c",
    "entity_id": "bank_of_america",
    "currency": "USD",
    "amount": 100.00,
    "balance": 150.00
  },
  {
    "id": "dad2c4a9-e521-4fb4-8536-3753a957d68c",
    "created_at": "2022-02-07T17:56:10.937758-05:00",
    "request_id": "e06cf58b-dc73-4d55-8ee5-1df243cbc739",
    "requested_at": "2022-02-07T17:56:10.758377-05:00",
    "transaction_id": "9d3f0c95-8f0d-41c8-989b-2992036a256d",
    "entity_id": "bank_of_america",
    "currency": "USD",
    "amount": -150.00,
    "balance": 0.00
  }
]
```
