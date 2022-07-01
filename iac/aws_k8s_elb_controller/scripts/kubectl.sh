#!/bin/bash

# set -e
set -x
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd)

while getopts :d flag
do
    case "${flag}" in
        d) DeleteResources=1;;
    esac
done

# Deploy load-balancer-controller
if [[ "$DeleteResources"  == 1 ]]; then
    cat ${SCRIPT_DIR}/${TEMPLATE_FILE} \
    | sed "s|{{CLUSTER_NAME}}|${CLUSTER_NAME}|g" \
    | sed "s|{{IAM_ROLE_ARN}}|${IAM_ROLE_ARN}|g" \
    | kubectl delete --ignore-not-found=true -f - || true
else
    cat ${SCRIPT_DIR}/${TEMPLATE_FILE} \
    | sed "s|{{CLUSTER_NAME}}|${CLUSTER_NAME}|g" \
    | sed "s|{{IAM_ROLE_ARN}}|${IAM_ROLE_ARN}|g" \
    | kubectl apply -f -
fi
