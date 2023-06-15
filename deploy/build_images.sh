#!/bin/bash

AWS_ACCOUNT="370056820766"
AWS_REGION="us-east-1"

################
# Get ENV VARS #
################
export $(grep -v '^#' ../.env | xargs)

########################
# Sign into ECR Docker #
########################
aws ecr get-login-password --region ${AWS_REGION} | docker login --username \
    AWS --password-stdin ${AWS_ACCOUNT}.dkr.ecr.${AWS_REGION}.amazonaws.com

#######################
# Get versioning info #
#######################
COMMIT_HASH=$(git rev-parse --short HEAD)

################
# Backend push #
################
BACKEND_ECR_REPO="370056820766.dkr.ecr.us-east-1.amazonaws.com/tinynakji-backend"
docker build \
    -t ${BACKEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${BACKEND_ECR_REPO}:latest \
        ../application/backend
docker push ${BACKEND_ECR_REPO}:${COMMIT_HASH}
docker push ${BACKEND_ECR_REPO}:latest

#################
# Frontend push #
#################
FRONTEND_ECR_REPO="370056820766.dkr.ecr.us-east-1.amazonaws.com/tinynakji-frontend"
docker build \
    --build-arg API_PATH \
    -t ${FRONTEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${FRONTEND_ECR_REPO}:latest \
     ../application/frontend
docker push ${FRONTEND_ECR_REPO}:${COMMIT_HASH}
docker push ${FRONTEND_ECR_REPO}:latest