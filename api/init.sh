#!/bin/bash

set -e

echo "Starting FastAPI app initialization..."

# AWS credentials are assumed to be configured in the container or via IAM role
export AWS_REGION=us-east-1

# Fetch secrets from AWS Secrets Manager / SSM
export ELASTICSEARCH_PASSWORD=$(aws secretsmanager get-secret-value --secret-id /cicd/expr_ops/ELASTICSEARCH_PASSWORD --query SecretString --output text | jq -r '."/cicd/expr_ops/ELASTICSEARCH_PASSWORD"')
export ELASTICSEARCH_ENDPOINT=$(aws ssm get-parameter --name /cicd/expr_ops/ELASTICSEARCH_ENDPOINT --with-decryption --query Parameter.Value --output text)
export ELASTICSEARCH_USERNAME=$(aws ssm get-parameter --name /cicd/expr_ops/ELASTICSEARCH_USERNAME --with-decryption --query Parameter.Value --output text)
export OPENAI_API_KEY=$(aws secretsmanager get-secret-value --secret-id /openai/apikey --query SecretString --output text | jq -r '."/openai/apikey"')

export PG_USER=$(aws secretsmanager get-secret-value \
  --secret-id 'rds!cluster-38ceda55-f63a-4ace-a21c-715ceed89a44' \
  --query SecretString \
  --output text | jq -r '.username')
export PG_PASSWORD=$(aws secretsmanager get-secret-value \
  --secret-id 'rds!cluster-38ceda55-f63a-4ace-a21c-715ceed89a44' \
  --query SecretString \
  --output text | jq -r '.password')
export PG_HOST=$(aws secretsmanager get-secret-value \
  --secret-id '/gen/rds/conn' \
  --query SecretString \
  --output text | jq -r '.host')
export PG_PORT=$(aws secretsmanager get-secret-value \
  --secret-id '/gen/rds/conn' \
  --query SecretString \
  --output text | jq -r '.port')
export PG_DB=$(aws secretsmanager get-secret-value \
  --secret-id '/gen/rds/conn' \
  --query SecretString \
  --output text | jq -r '.dbname')
export EXPR_CUSTOMERS_ORG_GITHUB_TOKEN=$(aws secretsmanager get-secret-value --secret-id /cicd/customers-org/githubtoken --query SecretString --output text | jq -r '."/cicd/customers-org/githubtoken"')

# Build DATABASE_URL from PG vars
export DATABASE_URL="postgresql://$PG_USER:$PG_PASSWORD@$PG_HOST:$PG_PORT/$PG_DB"

echo "Launching FastAPI app..."
uvicorn main:app --host 0.0.0.0 --port 8000
