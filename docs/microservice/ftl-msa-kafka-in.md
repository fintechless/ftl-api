# ftl-msa-kafka-in

## Description

Kafka In MSA consumes specific outgoing Kafka topic
and submits to Message In MSA as incoming XML messages.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: protected
- [x] OAuth Scope: n/a
- [x] HTTP Method: n/a
- [x] HTTP URL: n/a

## Workflow

- [x] receive XML message from specific outgoing topic (Kafka provider)
- [x] receive X-Transaction-Id from UUID MSA using POST method (HTTP provider)
- [x] send XML message to Message In MSA using POST method (HTTP provider)
  * if success, mark XML message consumed in outgoing topic (Kafka provider)
  * if failed, retry previous step using exponential backoff; repeat up to 3 times
- [x] if still failed, make sure that XML message IS NOT consumed in outgoing topic (Kafka provider)
