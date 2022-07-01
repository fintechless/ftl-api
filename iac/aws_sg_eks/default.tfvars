src = {
  name        = "ftl-eks-cluster-sg"
  description = "VPC Security Group used by the Fintchless EKS cluster"

  vpc_tags = {
    Name = "shared"
  }

  rules = {
    self = {
      type      = "ingress"
      from_port = -1
      to_port   = -1
      protocol  = "-1"
      self      = true
    },
    microservices = {
      type        = "ingress"
      from_port   = 5000
      to_port     = 5100
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    },
    prometheus = {
      type        = "ingress"
      from_port   = 9090
      to_port     = 9090
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}
