#!/bin/bash

# A simple smoke test script to verify app health
# In a real scenario, this would curl the 'Green' Load Balancer URL

echo "Checking application health..."

# Mocking a health check request
RESPONSE="200"

if [ "$RESPONSE" == "200" ]; then
  echo "✅ Green Environment is Healthy! Traffic switch approved."
  exit 0
else
  echo "❌ Green Environment Failed Smoke Test! Aborting deployment."
  exit 1
fi
