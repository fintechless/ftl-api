# ftl-msa-msg-client

## Description

Message Client MSA queries Latest MSA for "hanging" messages that are not consumed
within a predefined TTL. If successful, JSON object containing request_id (optional),
transaction_id (required) and timestamp (required) are sent to corresponding client:
either ActiveMQ Out MSA, or IBM MQ Out MSA, or RabbitMQ Out MSA.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: protected
- [x] OAuth Scope: n/a
- [x] HTTP Method: n/a
- [x] HTTP URL: n/a

## Workflow

TBU
