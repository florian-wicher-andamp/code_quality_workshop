#!/bin/bash

resourceGroupName="rg_qa_workshop"
subscription="ACS_Psaier_Energies_Development_1"
appName="banking-app"

echo "Creating resource group..."
az group create \
  --name $resourceGroupName \
  --location francecentral \
  --subscription $subscription \
  --tags purpose=qa_workshop

echo "Deploying infrastructure..."
az deployment group create \
  --resource-group $resourceGroupName \
  --template-file main.bicep \
  --subscription $subscription \
  --parameters functionAppName=$appName

echo "Deploying function app..."
func azure functionapp publish $appName --python