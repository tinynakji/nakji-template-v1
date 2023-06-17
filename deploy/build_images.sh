#!/bin/bash

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
docker build \
    -t ${BACKEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${BACKEND_ECR_REPO}:latest \
        ../application/backend
docker push ${BACKEND_ECR_REPO}:${COMMIT_HASH}
docker push ${BACKEND_ECR_REPO}:latest

#################
# Frontend push #
#################
docker build \
    --build-arg API_PATH \
    -t ${FRONTEND_ECR_REPO}:${COMMIT_HASH} \
    -t ${FRONTEND_ECR_REPO}:latest \
     ../application/frontend
docker push ${FRONTEND_ECR_REPO}:${COMMIT_HASH}
docker push ${FRONTEND_ECR_REPO}:latest