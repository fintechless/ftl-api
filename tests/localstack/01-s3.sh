#!/bin/sh

set -e
set -x
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail

export AWS_ACCESS_KEY_ID=dummyaccess
export AWS_SECRET_ACCESS_KEY=dummysecret
export AWS_DEFAULT_REGION=us-east-1
export AWS_ACCOUNT_ID=123456789012
export FTL_ENVIRONMENT=default

aws s3api create-bucket \
    --endpoint-url=http://localstack:4566 \
    --bucket ftl-api-runtime-${FTL_ENVIRONMENT}-${AWS_DEFAULT_REGION}-${AWS_ACCOUNT_ID}
