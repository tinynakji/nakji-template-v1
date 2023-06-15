#!/bin/bash

kubectl apply \
    -f backend/deployment.yaml \
    -f backend/service.yaml \
    -f frontend/deployment.yaml \
    -f frontend/service.yaml
