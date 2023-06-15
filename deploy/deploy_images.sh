#!/bin/bash

kubectl apply \
    -f kube/backend/deployment.yaml \
    -f kube/backend/service.yaml \
    -f kube/frontend/deployment.yaml \
    -f kube/frontend/service.yaml
