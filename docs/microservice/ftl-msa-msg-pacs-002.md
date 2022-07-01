# ftl-msa-msg-pacs-002

## Description

Message PACS 002 MSA consumes internal specific incoming messages,
validates business rules and executes business specific logic.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: protected
- [x] OAuth Scope: n/a
- [x] HTTP Method: n/a
- [x] HTTP URL: n/a

## Workflow

- [x] receive internal message from target resource resulted from Mapping MSA (e.g. source=ftl-msa-msg-pacs-002, source_type=message_in, content_type=text/xml, message_type=pacs.002)
  * send pacs-002 message to target resource resulted from Mapping MSA (e.g. source=ftl-msa-msg-pacs-002, source_type=message_out, content_type=text/xml, message_type=pacs.002)
  * send NOTIFIED status to transaction table (NoSQL provider)
- [x] validate business specific rules (HTTP provider)
- [x] execute business specific logic (HTTP provider)
- [x] if success, update the following targets:
  * send NOTIFIED status to transaction table (NoSQL provider)
- [x] if failed, update the following targets:
  * send REJECTED status to transaction table (NoSQL provider)
