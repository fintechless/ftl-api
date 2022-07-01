# MicroService Architecture

## CATEGORY: PLATFORM

MicroService | Type | Scope | Method | URL | Health Check | Details
-------------|------|-------|--------|-----|--------------|--------
ftl-api-ping | public | public.read | GET | / | - | [ftl-api-ping.md](ftl-api-ping.md)
ftl-api-ping-cache | public | public.read | GET | /ping/cache | - | [ftl-api-ping-cache.md](ftl-api-ping.md)
ftl-api-ping-nosql | public | public.read | GET | /ping/nosql | - | [ftl-api-ping-nosql.md](ftl-api-ping.md)
ftl-api-ping-sql | public | public.read | GET | /ping/sql | - | [ftl-api-ping-sql.md](ftl-api-ping.md)
ftl-api-ping-storage | public | public.read | GET | /ping/storage | - | [ftl-api-ping-storage.md](ftl-api-ping.md)
ftl-api-uuid | public | public.write | POST | /uuid | /uuid/_healthy | [ftl-api-uuid.md](ftl-api-uuid.md)
ftl-api-status | public | public.read | GET | /status | /status/_healthy | [ftl-api-status.md](ftl-api-status.md)
ftl-api-latest | public | public.read | GET | /latest | /latest/_healthy | [ftl-api-latest.md](ftl-api-latest.md)
ftl-api-mapping | private | private.read | GET | /mapping | /mapping/_healthy | [ftl-api-mapping.md](ftl-api-mapping.md)
ftl-api-entity | private | private.read | GET | /entity | /entity/_healthy | [ftl-api-entity.md](ftl-api-entity.md)

## CATEGORY: MICROSERVICE

MicroService | Type | Scope | Method | URL | Health Check | Details
-------------|------|-------|--------|-----|--------------|--------
ftl-msa-msg-in | public | public.write | POST | / | /msa/in/_healthy | [ftl-msa-msg-in.md](ftl-msa-msg-in.md)
ftl-msa-msg-out | private | private.write | POST | /msa/out | /msa/out/_healthy | [ftl-msa-msg-out.md](ftl-msa-msg-out.md)
ftl-msa-msg-client | protected | - | - | - | - | [ftl-msa-msg-client.md](ftl-msa-msg-client.md)
ftl-msa-msg-pacs-002 | protected | - | - | - | - | [ftl-msa-msg-pacs-002.md](ftl-msa-msg-pacs-002.md)
ftl-msa-msg-pacs-008 | protected | - | - | - | - | [ftl-msa-msg-pacs-008.md](ftl-msa-msg-pacs-008.md)
ftl-msa-msg-pacs-009 | protected | - | - | - | - | [ftl-msa-msg-pacs-009.md](ftl-msa-msg-pacs-009.md)
ftl-msa-amq-in | protected | - | - | - | - | [ftl-msa-amq-in.md](ftl-msa-amq-in.md)
ftl-msa-amq-out | private | private.write | POST | /msa/amq | /msa/amq/_healthy | [ftl-msa-amq-out.md](ftl-msa-amq-out.md)
ftl-msa-imq-in | protected | - | - | - | - | [ftl-msa-imq-in.md](ftl-msa-imq-in.md)
ftl-msa-imq-out | private | private.write | POST | /msa/imq | /msa/imq/_healthy | [ftl-msa-imq-out.md](ftl-msa-imq-out.md)
ftl-msa-kafka-in | protected | - | - | - | - | [ftl-msa-kafka-in.md](ftl-msa-kafka-in.md)
ftl-msa-kafka-out | private | private.write | POST | /msa/kafka | /msa/kafka/_healthy | [ftl-msa-kafka-out.md](ftl-msa-kafka-out.md)
ftl-msa-pubsub-in | protected | - | - | - | - | [ftl-msa-pubsub-in.md](ftl-msa-pubsub-in.md)
ftl-msa-pubsub-out | private | private.write | POST | /msa/pubsub |/msa/pubsub/_healthy | [ftl-msa-pubsub-out.md](ftl-msa-pubsub-out.md)
ftl-msa-rmq-in | protected | - | - | - | - | [ftl-msa-rmq-in.md](ftl-msa-rmq-in.md)
ftl-msa-rmq-out | private | private.write | POST | /msa/rmq | /msa/rmq/_healthy | [ftl-msa-rmq-out.md](ftl-msa-rmq-out.md)

## CATEGORY: MANAGEMENT

MicroService | Type | Scope | Method | URL | Health Check | Details
-------------|------|-------|--------|-----|--------------|--------
ftl-mgr-message | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/message | /mgr/message/_healthy | [ftl-mgr-message.md](ftl-mgr-message.md)
ftl-mgr-message-category | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/message/category | /mgr/message/category/_healthy | [ftl-mgr-message-category.md](ftl-mgr-message-category.md)
ftl-mgr-message-parser | private | mgr.write | POST | /mgr/message/parser | /mgr/message/parser/_healthy | [ftl-mgr-message-parser.md](ftl-mgr-message-parser.md)
ftl-mgr-microservice | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/microservice | /mgr/microservice/_healthy | [ftl-mgr-microservice.md](ftl-mgr-microservice.md)
ftl-mgr-transaction | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/transaction | /mgr/transaction/_healthy | [ftl-mgr-transaction.md](ftl-mgr-transaction.md)
ftl-mgr-member | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/member | /mgr/member/_healthy | [ftl-mgr-member.md](ftl-mgr-member.md)
ftl-mgr-account | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/account | /mgr/account/_healthy | [ftl-mgr-account.md](ftl-mgr-account.md)
ftl-mgr-platform | public | mgr.read,mgr.write | GET,POST,PATCH,DELETE | /mgr/platform | /mgr/platform/_healthy | [ftl-mgr-platform.md](ftl-mgr-platform.md)

## CATEGORY: BI & ANALYTICS

MicroService | Type | Scope | Method | URL | Health Check | Details
-------------|------|-------|--------|-----|--------------|--------
tbd | public | bi.read | GET | /bi/tbu | - | -
tbd | public | bi.write | POST | /bi/tbu | /bi/tbu/_healthy | -
tbd | private | bi.read | GET | /bi/tbu | - | -
tbd | private | bi.write | POST | /bi/tbu | /bi/tbu/_healthy | -
