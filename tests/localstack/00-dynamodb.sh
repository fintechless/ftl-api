#!/bin/sh

set -e
set -x
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail

export AWS_ACCESS_KEY_ID=dummyaccess
export AWS_SECRET_ACCESS_KEY=dummysecret
export AWS_DEFAULT_REGION=us-east-1

aws dynamodb create-table \
--endpoint-url=http://localstack:4566 \
--table-name ftl-api-transaction-default \
--attribute-definitions AttributeName=id,AttributeType=S AttributeName=transaction_id,AttributeType=S AttributeName=status,AttributeType=S AttributeName=created_at,AttributeType=S \
--key-schema AttributeName=id,KeyType=HASH AttributeName=created_at,KeyType=RANGE \
--global-secondary-indexes \
    "[
        {
            \"IndexName\": \"gsi-transactionid\",
            \"KeySchema\": [
                {\"AttributeName\":\"transaction_id\",\"KeyType\":\"HASH\"},
                {\"AttributeName\":\"created_at\",\"KeyType\":\"RANGE\"}
            ],
            \"Projection\": {
                \"ProjectionType\":\"INCLUDE\",
                \"NonKeyAttributes\":[\"id\",\"created_at\",\"status\"]
            },
            \"ProvisionedThroughput\": {
                \"ReadCapacityUnits\": 5,
                \"WriteCapacityUnits\": 5
            }
        },
        {
            \"IndexName\": \"gsi-status\",
            \"KeySchema\": [
                {\"AttributeName\":\"status\",\"KeyType\":\"HASH\"},
                {\"AttributeName\":\"transaction_id\",\"KeyType\":\"RANGE\"}
            ],
            \"Projection\": {
                \"ProjectionType\":\"INCLUDE\",
                \"NonKeyAttributes\":[\"id\",\"transaction_id\",\"created_at\"]
            },
            \"ProvisionedThroughput\": {
                \"ReadCapacityUnits\": 5,
                \"WriteCapacityUnits\": 5
            }
        }
      ]" \
--provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
