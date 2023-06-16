#!/bin/bash

################
# Get ENV VARS #
################
export $(grep -v '^#' ../.env | xargs)

envsubst < kube/backend/deployment-template.yaml > kube/backend/deployment.yaml
envsubst < kube/backend/service-template.yaml > kube/backend/service.yaml
envsubst < kube/frontend/deployment-template.yaml > kube/frontend/deployment.yaml
envsubst < kube/frontend/service-template.yaml > kube/frontend/service.yaml

envsubst < kube/ingress/ingress-template.yaml > kube/ingress/ingress.yaml

# kubectl apply \
#     -f kube/backend/deployment.yaml \
#     -f kube/backend/service.yaml \
#     -f kube/frontend/deployment.yaml \
#     -f kube/frontend/service.yaml
