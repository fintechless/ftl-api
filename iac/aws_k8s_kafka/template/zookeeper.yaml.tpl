apiVersion: platform.confluent.io/v1beta1
kind: Zookeeper
metadata:
  name: zookeeper
  namespace: confluent
spec:
  replicas: 1
  image:
    application: confluentinc/cp-zookeeper:7.0.1
    init: confluentinc/confluent-init-container:2.2.1
  dataVolumeCapacity: 25Gi
  logVolumeCapacity: 15Gi
  podTemplate:
    affinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
            - matchExpressions:
                - key: eks.amazonaws.com/nodegroup
                  operator: In
                  values:
                    - ${EKS_NODE_GROUP}
    tolerations:
      - key: reserved-pool
        value: "true"
        operator: Equal
        effect: NoSchedule
