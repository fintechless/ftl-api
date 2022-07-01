# ftl-msa-rmq-out

## Description

RabbitMQ Out MSA exposes HTTP listener that receives JSON object that includes
request_id (optional), transaction_id (required) and timestamp (required). Further,
these parameters are sent to Status MSA and expected to receive outgoing XML message,
which is submitted to RabbitMQ incoming queue.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: private
- [x] OAuth Scope: private.write
- [x] HTTP Method: POST
- [x] HTTP URL: /msa/rmq

## Workflow

- [x] receive JSON object as HTTP request body using POST method (HTTP provider)
- [x] retrieve XML message from Status MSA using GET method (HTTP provider)
- [x] send XML message to specific incoming queue (RabbitMQ provider)
  * if failed, retry previous step using exponential backoff; repeat up to 3 times
- [x] if still failed, make sure to send FAILED status to transaction table (NoSQL provider)
- [x] send request_id, status and message as HTTP response (HTTP provider)
  * send pacs.002 internal format to service provider associated with outgoing messages from Mapping MSA (Kafka provider)
