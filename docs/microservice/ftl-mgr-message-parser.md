# ftl-mgr-message-parser

## Description

Message Parser MSA exposes HTTP listener that receives empty request and
updates the Message Definition table with new and/or updated message mappings.

## Characteristics

- [x] Category: Management
- [x] MSA Type: private
- [x] OAuth Scope: mgr.write
- [x] HTTP Method: POST
- [x] HTTP URL: /mgr/message/parser

## Workflow

- [x] Query Message Metadata table (e.g. ftl-api-message) and retrieve all paths for active XSD files
- [x] Parse each XSD file and retrieve all possible keys
- [x] For each key, verify if DOESN'T exists, then add into Message Definition table (e.g. ftl-api-message-definition)
