{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "${iam_openid_connect_provider_arn}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "${oidc_issuer_sub}": "system:serviceaccount:kube-system:aws-load-balancer-controller",
          "${oidc_issuer_aud}": "sts.amazonaws.com"
        }
      }
    }
  ]
}
