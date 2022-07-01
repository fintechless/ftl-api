#!/bin/bash

# set -e
set -x
# only exit with zero if all commands of the pipeline exit successfully
set -o pipefail

if [ -z "${1}" ]; then
  echo "[ERROR] Inline value for 'CLUSTER_NAME' is missing. Aborting..."
  exit 1
fi

CWD="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
aws eks update-kubeconfig --name ${1}

kubectl create namespace confluent

# helm repo add confluentinc https://packages.confluent.io/helm
# helm repo update

# helm pull confluentinc/confluent-for-kubernetes --untar
# kubectl apply -f confluent-for-kubernetes/crds/

helm upgrade -i confluent-operator confluentinc/confluent-for-kubernetes --namespace confluent --set debug="true"
