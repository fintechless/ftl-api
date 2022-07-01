# ftl-msa-msg-out

## Description

Message Out MSA exposes HTTP listener that receives internal format. If Kafka provider
is enabled, internal format can also be consumed from specific outgoing topic. Furthermore,
internal format is transformed into XML message and a copy is archived. If successful,
JSON object containing request_id, transaction_id and timestamp is sent to internal SNS
notification topic.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: private
- [x] OAuth Scope: private.write
- [x] HTTP Method: POST
- [x] HTTP URL: /msg/out

## Workflow

- [x] receive internal format as HTTP request body using POST method (HTTP provider)
- [x] retrieve Content-Type from HTTP header (HTTP provider)
- [x] retrieve mapping from Mapping MSA associated with message type identified from parsing (HTTP provider)
- [x] transform internal format into outgoing XML message (e.g. JSON2XML)
- [x] send XML message to storage bucket using the pattern from below (Storage provider)
  * storage_path: {bucket_name}/out/{year}/{month}/{day}/{hour}/{minute}/{second}/{millisecond_by_hundreds}{if_not_gmt_then_timezone_as_digits}/{uuid}.{content-type:xml/json}
  * if failed, retry this step using exponential backoff; repeat up to 3 times
- [x] if success, update the following targets:
  * send transformed message to target resource resulted from Mapping MSA (e.g. source=ftl-msa-msg-out, source_type=message_out, content_type=text/xml, message_type=pacs.008)
  * send RELEASED status to transaction table (NoSQL provider)
- [x] if failed, update the following targets:
  * send transformed message to target resource resulted from Mapping MSA (e.g. source=ftl-msa-msg-out, source_type=message_out, content_type=text/xml, message_type=pacs.002)
  * send FAILED status to transaction table (NoSQL provider)
- [x] send request_id, status and message as HTTP response (HTTP provider)
