# ftl-api-uuid

## Description

UUID MSA exposes HTTP listener that receives empty request and returns
newly INITIATED transaction, including transaction_id and request_id.

## Characteristics

- [x] Category: Platform
- [x] MSA Type: public
- [x] OAuth Scope: public.write
- [x] HTTP Method: POST
- [x] HTTP URL: /uuid

## Workflow

- [x] receive empty request as HTTP request body using POST method (HTTP provider)
- [x] generate uuid to be used as X-Transaction-Id
- [x] send INITIATED status and uuid as transation_id to transaction table as conditional write (NoSQL provider)
  * if failed, retry previous 2 steps using exponential backoff; repeat up to 3 times
- [x] send id (aka request id), uuid (aka transaction id), status and message as HTTP response (HTTP provider)
