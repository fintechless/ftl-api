# ftl-mgr-message-category

## Description

Message Category MSA exposes HTTP listener that receives empty request and
updates the Message Metadata table with new and/or updated message definitions.

## Characteristics

- [x] Category: Management
- [x] MSA Type: private
- [x] OAuth Scope: mgr.write
- [x] HTTP Method: POST
- [x] HTTP URL: /mgr/message/category

## Workflow

- [x] Parse ISO 20022 message definitions from official website (e.g. https://www.iso20022.org/iso-20022-message-definitions?page=0 and https://www.iso20022.org/iso-20022-message-definitions?page=1)
- [x] For each XSD, verify if DOESN'T exists in Message Metadata table (e.g. ftl-api-message)
- [x] Download each XSD file and store it in storage bucket (e.g. ftl-api-deploy-{region}-{account}/deploy/fintechless/ftl-api/schema/xsd/{iso20022_message_id}.xsd)
- [x] Save path for each storage object in Message Metadata table (e.g. ftl-api-message)
