apiVersion: platform.confluent.io/v1beta1
kind: ControlCenter
metadata:
  name: controlcenter
  namespace: confluent
spec:
  replicas: 1
  image:
    application: confluentinc/cp-enterprise-control-center:7.0.1
    init: confluentinc/confluent-init-container:2.2.1
  dataVolumeCapacity: 10Gi
  # dependencies:
    # schemaRegistry:
    #   url: http://schemaregistry.confluent.svc.cluster.local:8081
    # ksqldb:
    # - name: ksqldb
    #   url: http://ksqldb.confluent.svc.cluster.local:8088
    # connect:
    # - name: connect
    #   url: http://connect.confluent.svc.cluster.local:8083
  configOverrides:
    server:
      - confluent.controlcenter.internal.topics.replication=1
      - confluent.controlcenter.command.topic.replication=1
      - confluent.monitoring.interceptor.topic.replication=1
      - confluent.metrics.topic.replication=1
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
