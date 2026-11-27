# AI Code Detective - Architecture Overview

## 1. Project Overview

AI Code Detective is an AI-powered platform that investigates
software repositories, identifies potential bugs, analyzes root
causes, generates fixes, and validates proposed patches.

## 2. Backend Technology

- Python
- FastAPI
- Pydantic Settings
- Boto3
- Pytest
- Ruff

## 3. AWS Architecture

- Amazon DynamoDB: Application metadata and workflow state
- Amazon S3: Reports and generated artifacts
- AWS Lambda: API and short-running background operations
- Amazon ECS Fargate: Isolated repository execution
- AWS Step Functions: Workflow orchestration
- Amazon SQS: Asynchronous messaging
- Amazon CloudWatch: Monitoring and logs

## 4. Application Design

We will begin with a modular monolith.

Major application modules:

- Repository management
- Code intelligence
- AI agents
- Patch generation
- Validation
- GitHub integration

Modules will have clear boundaries so they can be extracted
into independent services if required later.

## 5. AI Workflow

1. Register a GitHub repository.
2. Inspect and analyze its source code.
3. Identify potential bugs.
4. Investigate root causes.
5. Generate proposed patches.
6. Validate patches in an isolated environment.
7. Create GitHub issues and pull requests for human review.

## 6. Security

- Never execute untrusted repository code inside the API process.
- Use isolated execution environments for builds and tests.
- Keep credentials in secure secret storage.
- Treat repository content as untrusted input.
- Require human approval before merging patches.

## 7. Development Principles

- Feature-based Git branches.
- Pull requests for every logical feature.
- Automated tests and linting.
- Infrastructure managed using Terraform.