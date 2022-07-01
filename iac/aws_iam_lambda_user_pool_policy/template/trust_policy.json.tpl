{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "cognito-idp:ListUserPoolClients",
        "cognito-idp:DescribeUserPoolClient"
      ],
      "Resource": ["${user_pool_arn}"],
      "Effect": "Allow"
    }
  ]
}
