#!/bin/bash

################
# Get ENV VARS #
################
export $(grep -v '^#' ../.env | xargs)
envsubst < kube/ingress/ingress-template.yaml > kube/ingress/ingress.yaml
