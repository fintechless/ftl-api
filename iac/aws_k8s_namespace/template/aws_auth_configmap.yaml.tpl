apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    %{ for name in role_names }
    - rolearn: arn:aws:iam::${account_id}:role/${name}
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes
    %{ endfor ~}
    %{ for name in sso_users }
    - rolearn: arn:aws:iam::${account_id}:role/${name}
      username: ${name}
      groups:
        - system:bootstrappers
        - system:masters
    %{ endfor ~}
