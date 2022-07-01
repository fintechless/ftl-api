# Guiding Principles

## Serverless First

Fintechless is the Serverless Platform for Financial Institutions and Fintechs.
By design, the platform is serverless first. But in some cases, the cloud
provider might not be offering a serverless solution (e.g. Kafka or IBM MQ).
Such solutions will be implemented and deployed on Kubernetes cloud native
service. Fintechless will later replace such solutions with cloud provider's
serverless version when it will become available.

## Low Latency and Cross Region

Fintechless is designed to provide low latency and cross-region capabilities.
In theory, providing both features at the same time is very difficult and
very expensive. In practice, only a small subset of data points requires both
low latency and cross region (e.g. transactions, liquidity, etc), while the
vast majority of data points can be replicated cross regions with acceptable
higher latency (e.g. messages, configs, mappings, etc). Beyond data services,
there is no need for realtime synchronization of cloud services like compute,
networking, dns, security, etc. This is the beauty of serverless platforms:
the same configs of cloud native services are deployed across active region and
passive region. In case of a disaster, the passive region becomes active
in a matter of seconds and effectively absorbs the entire workload with no
downtime.

## Inserts and Retrieves Only

Fintechless is intended to be the go-to platform in the Financial Industry.
The data points can be inserted into the platform and retrieved from the
platform. Any direct data updates on the platform are discouraged. Instead
of one update, perform two inserts: first insert to cancel updated record and
second insert to enable updated record. Deletes on the platform are welcomed
only if the data is offloaded into the storage service for longer term usage:
backup and restore, or backup and archive, or write-once-read-many patterns.

## Transaction vs Post-Transaction

Fintechless is focused on processing low latency transactions at scale without
compromising the availability and the reliability of the financial system. In
order to achieve these goals, post-transactional operations should be clearly
and deliberately decoupled from transactional operations. For example, get the
status of a current transaction to decide the next step of that transaction is
part of transactional process, while get the status of a historical transaction
is part of post-transactional process and should never be mixed. Similar logic
should be applied to every service and every process that involves application,
data, infrastructure, security, and everything in between.
