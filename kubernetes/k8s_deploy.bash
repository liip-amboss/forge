#!/bin/bash
echo "Deploying DB ..."
echo ""
kustomize build db | kubectl apply -f -
sleep 5
echo "Deploying App ..."
echo ""
kustomize build backend | kubectl apply -f -
kustomize build frontend | kubectl apply -f -
sleep 5
echo "Deploying Migration Job ..."
echo ""
kustomize build migration-job | kubectl delete -f -
kustomize build migration-job | kubectl apply -f -
