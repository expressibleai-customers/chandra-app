#!/bin/bash
set -e

# Configuration
IMAGE_NAME="generated-ui"
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="132717948683"
ECR_REPO="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/expressible:$IMAGE_NAME"

APP_PATH="$(pwd)"

echo "📦 Building Docker image..."
docker build -t $IMAGE_NAME $APP_PATH --progress plain --no-cache

echo "🔐 Logging in to AWS ECR..."
aws ecr get-login-password --region $AWS_REGION | \
    docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

echo "🚀 Tagging and pushing image..."
docker tag $IMAGE_NAME $ECR_REPO
docker push $ECR_REPO

echo "🧹 Cleaning up local image..."
docker rmi $IMAGE_NAME $ECR_REPO || true
docker image prune -f

echo "✅ Docker build and push complete!"
