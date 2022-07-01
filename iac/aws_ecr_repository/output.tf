output "url" {
  value = tomap({
    for url, repository in aws_ecr_repository.this : reverse(split("/", url))[0] => repository.repository_url
  })
}
