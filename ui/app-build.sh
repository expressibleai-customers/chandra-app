#!/bin/bash
set -e

echo "🔧 Starting Angular build..."

APP_PATH="$(pwd)"
cd "$APP_PATH"

echo "🧹 Cleaning old files..."
rm -rf node_modules/ dist/

echo "📦 Installing deps..."
npm ci

echo "🏗️ Building Angular app..."
npm run build -- --configuration production --base-href=/

echo "✅ Angular build complete."
