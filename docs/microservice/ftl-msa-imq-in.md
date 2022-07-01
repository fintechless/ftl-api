# ftl-msa-imq-in

## Description

IBM MQ In MSA consumes specific outgoing IBM MQ queue
and submits to Message In MSA as incoming XML messages.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: protected
- [x] OAuth Scope: n/a
- [x] HTTP Method: n/a
- [x] HTTP URL: n/a

## Workflow

- [x] receive XML message from specific outgoing queue (IBM MQ provider)
- [x] receive X-Transaction-Id from UUID MSA using POST method (HTTP provider)
- [x] send XML message to Message In MSA using POST method (HTTP provider)
  * if success, mark XML message consumed in outgoing queue (IBM MQ provider)
  * if failed, retry previous step using exponential backoff; repeat up to 3 times
- [x] if still failed, make sure that XML message IS NOT consumed in outgoing queue (IBM MQ provider)
