# ftl-api-status

## Description

Status MSA exposes HTTP listener that receives multiple query parameters
and returns XML message if result includes exactly one XML message.

## Characteristics

- [x] Category: Platform
- [x] MSA Type: public
- [x] OAuth Scope: public.read
- [x] HTTP Method: GET
- [x] HTTP URL: /status

## Workflow

- [x] receive transaction_id (required), timestamp (required), request_id (optional), message_type (optional) and incoming (optional) as HTTP query parameter using GET method (HTTP provider)
  * default value for incoming is false, which means message's storage_path will be prefixed by `out/`
  * if incoming is true, message's storage_path will be prefixed by `in/`
- [x] retrieve transaction_id from transaction table (NoSQL provider)
- [x] retrieve XML message from storage bucket (Storage provider)
- [x] send RETRIEVED status to transaction table (NoSQL provider)
- [x] update `retrieved_at={datetime}` attribute associated with either RELEASED, REJECTED, CANCELED or NOTIFIED status in transaction table (NoSQL provider)
- [x] send XML message as HTTP response (HTTP provider)
