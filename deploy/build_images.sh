#!/bin/bash

docker build -t nakji_deploy_api:latest ../application/backend

# List of build args needed for UI Docker image build

docker build -t nakji_deploy_ui:latest ../application/frontend