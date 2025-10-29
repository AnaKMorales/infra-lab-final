#!/bin/bash

echo "🔨 Aplicando todos los manifiestos Kubernetes..."

# Namespace
kubectl apply -f namespace.yaml

# ConfigMaps
kubectl apply -f backend/configmap.yaml
kubectl apply -f notification-service/configmap.yaml

# Secrets
kubectl apply -f notification-service/secret.yaml

# Deployments
kubectl apply -f backend/deployment.yaml
kubectl apply -f notification-service/deployment.yaml
kubectl apply -f frontend/deployment.yaml

# Services
kubectl apply -f backend/service.yaml
kubectl apply -f notification-service/service.yaml
kubectl apply -f frontend/service.yaml

echo "Todos los recursos aplicados"
echo "Verificando estado:"
kubectl get all -n user-registration
