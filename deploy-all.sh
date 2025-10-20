#!/bin/bash
set -e

echo "🚀 Starting full deployment..."

# Build and push UI
echo "📦 [1/3] Building and pushing UI..."
cd ui
./docker-build-tag-push.sh
cd ..

# Build and push API
echo "📦 [2/3] Building and pushing API..."
cd api
./docker-build-tag-push.sh
cd ..

# Pull and run both
echo "🏃 [3/3] Deploying services..."
cd ui
./docker-pull-run.sh
cd ../api
./docker-pull-run.sh
cd ..

echo "✅ Deployment complete!"
echo ""
echo "Access your application:"
echo "  Frontend: http://localhost:4200"
echo "  API:      http://localhost:8000/docs"
