#!/bin/bash
set -e

# Configuration
IMAGE_NAME="generated-api"
CONTAINER_NAME="generated-api"
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="132717948683"
ECR_IMAGE="$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/expressible:$IMAGE_NAME"
NETWORK_NAME="gen"
PORT="8000"

echo "🔐 Logging in to AWS ECR..."
aws ecr get-login-password --region $AWS_REGION | \
    docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

echo "⬇️ Pulling image..."
docker pull $ECR_IMAGE

# Ensure docker network exists
docker network inspect $NETWORK_NAME >/dev/null 2>&1 || \
    docker network create $NETWORK_NAME

echo "🛑 Stopping old container (if any)..."
docker stop $CONTAINER_NAME 2>/dev/null || true
docker rm $CONTAINER_NAME 2>/dev/null || true

echo "🚀 Running new container..."
docker run -d \
  --net $NETWORK_NAME \
  --name $CONTAINER_NAME \
  -p $PORT:8000 \
  $ECR_IMAGE

echo "✅ Container running on http://localhost:$PORT"
echo "📖 API docs: http://localhost:$PORT/docs"
