#!/bin/bash

#####################
# Get namespace arg #
#####################
# if [ $# -eq 0 ]
#   then
#     echo "No namespace supplied"
#     exit 1
# fi

################
# Get ENV VARS #
################
export $(grep -v '^#' ../.env | xargs)

#######################
# Get versioning info #
#######################
export COMMIT_HASH=$(git rev-parse --short HEAD)
export BACKEND_IMAGE_URL=$BACKEND_ECR_REPO:$COMMIT_HASH
export FRONTEND_IMAGE_URL=$FRONTEND_ECR_REPO:$COMMIT_HASH

####################
# Kubernetes stuff #
####################
NAMESPACE_ARG=""

if [ -n $NAMESPACE ]; then NAMESPACE_ARG="-n $NAMESPACE"; fi

######################
# Compile kube files #
######################
envsubst < kube/backend/deployment-template.yaml > kube/backend/deployment.yaml
envsubst < kube/backend/service-template.yaml > kube/backend/service.yaml
envsubst < kube/frontend/deployment-template.yaml > kube/frontend/deployment.yaml
envsubst < kube/frontend/service-template.yaml > kube/frontend/service.yaml
# envsubst < kube/ingress/ingress-template.yaml > kube/ingress/ingress.yaml

#####################
# Deploy to cluster #
#####################
kubectl apply \
    -f kube/backend/deployment.yaml \
    -f kube/backend/service.yaml \
    -f kube/frontend/deployment.yaml \
    -f kube/frontend/service.yaml
