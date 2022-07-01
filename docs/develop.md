# Fintechless API

Serverless Platform for Financial Institutions and Fintechs

## Project architecture

The API is separated into microservices. Each microservice has it's own AWS ECR repository and K8s resources.
A microservice is comprised of the following K8s resources:

- Deployment (manages the base compute/pods where the microservices is running)
- Service (exposes the microservice as a service, which will be then attached to the `Ingress`)
- Ingress (manages the unique AWS ELB Load Balancer and ELB Target Groups in order to allow incoming traffic to the pods)

### Add a new microservice

If you wish to add a new microservice, the following steps should be followed:

#### Define the microservice's folder structure

Each microservice is a Flask application running in its own container.
In order to add a new microservice, you will need to create a new Flask application for it.

Please follow the following folder structure for your new microservice:

```text
ftl_api/msa/MICROSERVICE_NAME
├── __init__.py
├── blueprints
│   ├── __init__.py
│   └── MICROSERVICE_NAME.py > here should be defined the base Flask blueprint with the `/msa/MICROSERVICE_NAME` as URL prefix
├── .env > any environment variables used by the microservices
├── config.py > any configurations, which are loaded from the .env file, if present
├── run.py > here should be defined the Flask application, using the Flask Application Factory pattern
└── views
    ├── __init__.py
    ├── healthy.py > here should be defined the handlers for AWS ELB LB health checks
    └── root.py > here should be defined the handler for the requests coming to the root, which in our case would the URL prefix itself 
```

#### Create a new AWS ECR repository

All Docker images for each microservice are privately hosted in their specific AWS ECR repository.
For your new microservice, create a new repository where the Docker image will be stored (example provided [here](iac/aws_ecr_repository_msa_latest/main.tf))

#### Update `.dockercontainers` file

Each microservice has its own entry in the [`.dockercontainers`](.dockercontainers) file.
For your new microservice, add a new entry, as described below:

```yaml
msa:
  [...]
  MICROSERVICE_NAME:
    name: MICROSERVICE_ENTRYPOINT
    port: PORT_NUMBER
    health_check_path: HTTP_PATH_FOR_ELB_HEALTHCHECK
```

`MICROSERVICE_NAME` is the name of microservice, as indicated in the AWS ECR repository name: _ftl/msa/**NAME**_.

`MICROSERVICE_ENTRYPOINT` is the path to the microservice's code as a Python module. Should be in the following format: `ftl_api.msa.[MICROSERVICE_NAME].run`

`PORT_NUMBER` is the port the Flask application is running on. Must be an even number

`HTTP_PATH_FOR_ELB_HEALTHCHECK` is the HTTP path for the AWS ELB LB health checks

#### Create K8s resources

Your new microservice needs to have a `Deployment`, `Service` and `Ingress`.
The `Deployment` resource must use the Docker image from the AWS ECR repository

#### Create AWS ELB target group

In order to allow incoming traffic to your microservice, you must create an AWS ELB target group (example provided [here](iac/aws_lb_target_group_msa_status/main.tf)).

#### Attach the target group to the API's Network Load Balancer

Because the microservices are exposed in a private manner, the AWS ELB target group which was created in the previous
step needs to be attached to the API's Network Load Balancer (NLB).

In order to do so, please update [this](iac/aws_nlb_listener/locals.tf) Terraform component for NLB. Add any necessary Terraform state data sources.

## Local development environment

### Virtual environment

You'll need [poetry](https://python-poetry.org/docs/#installation). This Python repository uses `Poetry` for managing its packages and dependencies.
Exit from your current virtual environment, if activated. Execute the following command in order to install `Poetry`:

```shell
pip install poetry
```

It is recommended you create a separate virtual environment (Python >=3.10) using `venv`. In order to create
a new virtual environment, execute the following command:

```shell
poetry shell
```

### Dependencies

In order to install the dependencies execute the following command in your shell.

```shell
poetry install
```

If you need to add a new dependency for development, you can execute the following command in your shell.

```shell
poetry add <NAME> --dev
```

If you need to add a new required dependency, you can execute the following command in your shell.

```shell
poetry add <NAME>
```

## Build

If necessary, the Docker images can be built by executing the following command from the root of the project:

```shell
./bin/build.sh -e dev
```

### Tests

```shell
poetry run tests
```

## Code formatting

This library uses `black` in order to format the code using the PEP8 style guide. Execute the following command
to format the code (make sure to install all the dependencies with `Poetry`):

```shell
poetry run format
```

## Code linting

This library uses `pylint` to analyze the code in order to ensure that it's PEP8 compliant. Execute the following commands
to analyze the code (make sure to install all the dependencies with `Poetry`):

```shell
poetry run lint
```
