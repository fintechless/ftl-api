{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Principal": {
        "Federated": "cognito-identity.amazonaws.com"
      },
      "Effect": "Allow",
      "Condition": {
        "StringEquals": {
          "cognito-identity.amazonaws.com:aud": "${identity_pool_id}"
        }
      }
    }
  ]
}
