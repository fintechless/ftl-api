# Account

## Characteristics

- [x] Category: Management
- [x] Requirements: regional, mutable, cachable
- [x] Source: in-memory + rdbms
- [x] Identifier: ftl-mgr-account

## Definition

Name | Type | Required | Attributes | Details
-----|------|----------|------------|--------
id | varchar(36) | yes | primary | id, primary key using uuid function
reference_id | varchar(36) | yes | - | reference uuid, reference key for queries to filter our deleted records
child_id | varchar(36) | no | - | child uuid, reference key to new record that replaced deleted one
name | varchar(255) | no | - | "TBD"
email | varchar(255) | no | - | "TBD"
description | text | no | - | "TBD"
website | varchar(255) | no | - | "TBD"
member | text | no | - | "TBD"
created_at | timestamp | yes | - | date and time when record was created (iso datetime with milliseconds and timezone)
created_by | varchar(36) | yes | - | member uuid who created the record (reference key to member table)
deleted_at | timestamp | no | - | date and time when record was deleted (iso datetime with milliseconds and timezone)
deleted_by | varchar(36) | no | - | member uuid who deleted the record (reference key to member table)
TBD | - | - | - | -

## Examples

```json
{
  "id": "TBD"
}
```
