# ftl-api-latest

## Description

Latest MSA exposes HTTP listener that empty request and retuns a list of
transaction_id for active entity and a predefined list of statuses.

## Characteristics

- [x] Category: Platform
- [x] MSA Type: public
- [x] OAuth Scope: public.read
- [x] HTTP Method: GET
- [x] HTTP URL: /latest

## Workflow

- [x] receive empty body using GET method (HTTP provider)
- [x] retrieve for current oauth_entity the list of transaction_id from transaction table where status RELEASED, REJECTED, CANCELED or NOTIFIED && without `retrieved_at` attribute LIMIT 50 (NoSQL provider)
- [x] send the list of transaction_id, status and message as HTTP response (HTTP provider)
