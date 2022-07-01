# Message Definition

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, regional, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-message-definition

## Definition

Name | Type | Required | Attributes | Details
-----|------|----------|------------|--------
id | varchar(36) | yes | primary | id, primary key using uuid function
reference_id | varchar(36) | yes | - | reference uuid, reference key for queries to filter our deleted records
child_id | varchar(36) | no | - | child uuid, reference key to new record that replaced deleted one
created_at | timestamp | yes | - | date and time when record was created (iso datetime with milliseconds and timezone)
created_by | varchar(36) | yes | - | member uuid who created the record (reference key to member table)
deleted_at | timestamp | no | - | date and time when record was deleted (iso datetime with milliseconds and timezone)
deleted_by | varchar(36) | no | - | member uuid who deleted the record (reference key to member table)
activated_at | timestamp | no | - | date and time when record became active (iso datetime with milliseconds and timezone)
message_id | varchar(36) | yes | - | message uuid, foreign key to message table
xsd_tag | string | yes | - | xsd tag, element or attribute, used to retrieve the name and the type of the data field
name | string | yes | - | name of xsd tag (e.g. FIToFICstmrCdtTrf)
type | string | yes | - | type of xsd tag (e.g. FIToFICustomerCreditTransferV10)
annotation_name | string | no | - | annotation name to describe the xsd element
annotation_definition | string | no | - | annotation definition to describe the xsd element
parent_id | varchar(36) | yes | - | parent uuid, foreign key to itself (message definition table)
level | tinyint | yes | - | number of parents required to reach the root element of the xsd file
is_leaf | boolean | yes | - | only a leaf can be mapped to internal format
target_column | string | no | - | target column being mapped to the internal format
target_type | string | no | - | target type being mapped to the internal format

> NOTE: Unique constrain can be the combination of unique_key, activated_at and deleted_at

## Examples

id | reference_id | child_id | created_at | created_by | deleted_at | deleted_by | activated_at | message_id | xsd_tag | name | type | annotation_name | annotation_definition | parent_id | level | is_leaf | target_column | target_type
---|--------------|----------|------------|------------|------------|------------|--------------|------------|---------|------|------|----------------|-----------------------|-----------|-------|---------|---------------|------------
e01964f6-e7c1-4adc-9d29-ebd695959969 | e01964f6-e7c1-4adc-9d29-ebd695959969 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | Document | Document | - | -  | null | 0 | false| null | null
6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | FIToFICstmrCdtTrf | FIToFICustomerCreditTransferV10 | null | null | e01964f6-e7c1-4adc-9d29-ebd695959969 | 1 | false | - | -
d0c2e033-57af-458a-80a5-e4ab6f72dea0 | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | GrpHdr | GroupHeader96 | GroupHeader | Set of characteristics shared by all individual transactions included in the message. | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | 2 | false | null | null
ba04ac7d-88e0-4020-923b-abf3b382d7ac | ba04ac7d-88e0-4020-923b-abf3b382d7ac | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | MsgId | Max35Text | MessageIdentification | Point to point reference, as assigned by the instructing party, and sent to the next party in the chain to unambiguously identify the message.\nUsage: The instructing party has to make sure that MessageIdentification is unique per instructed party for a pre-agreed period. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
132a6d91-e978-4d71-8838-d82d730111ec | 132a6d91-e978-4d71-8838-d82d730111ec | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | CreDtTm | ISODateTime | CreationDateTime | Date and time at which the message was created. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
205d4f9c-6b42-4bd6-9609-8ba2d056d112 | 205d4f9c-6b42-4bd6-9609-8ba2d056d112 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | BtchBookg | BatchBookingIndicator | BatchBooking | Identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.\nUsage: Batch booking is used to request and not order a possible batch booking. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
f5733479-9287-48e9-ad25-41d1402c85fd | f5733479-9287-48e9-ad25-41d1402c85fd | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | NbOfTxs | Max15NumericText | NumberOfTransactions | Number of individual transactions contained in the message. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
8738b914-38d0-4a55-81f8-73cc05cf336b | 8738b914-38d0-4a55-81f8-73cc05cf336b | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | CtrlSum | DecimalNumber | ControlSum | Total of all individual amounts included in the message, irrespective of currencies. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
db5125ff-d0fb-47d6-aca6-ac2a912320f7 | db5125ff-d0fb-47d6-aca6-ac2a912320f7 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | TtlIntrBkSttlmAmt | ActiveCurrencyAndAmount | TotalInterbankSettlementAmount | Total amount of money moved between the instructing agent and the instructed agent. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
783c9b6e-3f82-4dc4-a43c-486d2476f7ac | 783c9b6e-3f82-4dc4-a43c-486d2476f7ac | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | IntrBkSttlmDt | ISODate | InterbankSettlementDate | Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | adddb8c7-9ad0-48ec-8f5c-4ff5cd267b78 | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | SttlmInf | SettlementInstruction11 | SettlementInformation | Specifies the details on how the settlement of the transaction(s) between the instructing agent and the instructed agent is completed. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | false | null | null
5ebfa54c-60e4-453c-b320-345a978a1a8f | 5ebfa54c-60e4-453c-b320-345a978a1a8f | null | 2022-02-07T17:56:07.937758-05:00 | 8dd25286-bd45-4244-8f23-6c964c12e30d | null | null | 2022-02-07T17:56:07.937758-05:00 | 6601b256-ab8b-4b8b-9fb2-92b6a8edb435 | element | SttlmMtd | SettlementMethod1Code | SettlementMethod | Method used to settle the (batch of) payment instructions. | d0c2e033-57af-458a-80a5-e4ab6f72dea0 | 3 | true | null | null
