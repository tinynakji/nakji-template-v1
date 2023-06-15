#!/bin/bash

COMMIT_HASH=$(git rev-parse --short HEAD)

BACKEND_ECR_REPO="370056820766.dkr.ecr.us-east-1.amazonaws.com/tinynakji-backend"
docker build \
    -t ${BACKEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${BACKEND_ECR_REPO}:latest \
        ../application/backend
docker push ${BACKEND_ECR_REPO}:${COMMIT_HASH}
docker push ${BACKEND_ECR_REPO}:latest

# List of build args needed for UI Docker image build

FRONTEND_ECR_REPO="370056820766.dkr.ecr.us-east-1.amazonaws.com/tinynakji-frontend"
docker build \
    -t ${FRONTEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${FRONTEND_ECR_REPO}:latest \
     ../application/frontend
docker push ${FRONTEND_ECR_REPO}:${COMMIT_HASH}
docker push ${FRONTEND_ECR_REPO}:latest