apiVersion: platform.confluent.io/v1beta1
kind: Kafka
metadata:
  name: kafka
  namespace: confluent
spec:
  replicas: 1
  image:
    application: confluentinc/cp-server:7.0.1
    init: confluentinc/confluent-init-container:2.2.1
  dataVolumeCapacity: 25Gi
  metricReporter:
    enabled: true
  configOverrides:
    server:
      - confluent.balancer.enable=true
      - confluent.balancer.heal.uneven.load.trigger=ANY_UNEVEN_LOAD
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
