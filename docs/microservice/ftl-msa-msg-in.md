# ftl-msa-msg-in

## Description

Message In MSA exposes HTTP listener that receives XML message, archives a copy and transforms into
internal format for futher processing. Additionally, XML message is validated against corresponding
ISO 20022 XSD, as well as checks the transaction_id if is expired or duplicated.

## Characteristics

- [x] Category: Microservice
- [x] MSA Type: public
- [x] OAuth Scope: public.write
- [x] HTTP Method: POST
- [x] HTTP URL: /

## Workflow

- [x] receive XML message as HTTP request body using POST method (HTTP provider)
- [x] retrieve X-Transaction-Id from HTTP header (HTTP provider)
- [x] retrieve Content-Type from HTTP header (HTTP provider)
- [x] send XML message to storage bucket using the pattern from below (Storage provider)
  * storage_path: {bucket_name}/in/{year}/{month}/{day}/{hour}/{minute}/{second}/{millisecond_by_hundreds}{if_not_gmt_then_timezone_as_digits}/{uuid}.{content-type:xml/json}
  * if failed, retry this step using exponential backoff; repeat up to 3 times
- [x] validate if X-Transaction-Id exists, is NOT a duplicate and timestamp difference is less than {FTL_MSA_UUID_TTL} seconds between status INITIATED and current date time (NoSQL provider)
- [x] retrieve XSD file from storage and parse + validate XML message against XSD (Storage provider)
- [x] retrieve mapping from Mapping MSA associated with message type identified from parsing (HTTP provider)
- [x] transform parsed XML message into internal format (e.g. XML2JSON)
- [x] if success, update the following targets:
  * send transformed message to target resource resulted from Mapping MSA (e.g. source=ftl-msa-msg-in, source_type=message_in, content_type=text/xml, message_type=pacs.008)
  * send RECEIVED status to transaction table (NoSQL provider)
- [x] if failed, update the following targets:
  * send failed message to target resource resulted from from Mapping MSA (e.g. source=ftl-msa-msg-in, source_type=message_out, content_type=text/xml, message_type=pacs.002)
  * send REJECTED status to transaction table (NoSQL provider)
- [x] send request_id, status and message as HTTP response (HTTP provider)
