# ftl-api-mapping

## Description

Mapping MSA exposes HTTP listener that receives multiple query parameters
and returns a list of mapping values.

## Characteristics

- [x] Category: Platform
- [x] MSA Type: public
- [x] OAuth Scope: public.read
- [x] HTTP Method: GET
- [x] HTTP URL: /mapping

## Workflow

- [x] receive key value pairs as HTTP request parameters using GET method (HTTP provider)
- [x] query Mapping table by received parameters (e.g. source, source_type, content_type, message_type) and retrieve target
- [x] send a list of values that includes query parameters and retrieved target as HTTP response (HTTP provider)
