@description('The name of the Azure Function App')
param functionAppName string

@description('The location for the Azure resources')
param location string = resourceGroup().location


resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'qa${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {}
}

resource appServicePlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: '${functionAppName}-plan'
  location: location
  sku: {
    tier: 'Dynamic'
    name: 'Y1'
  }
  properties: {
    reserved: true //important if you want to use linux
  }
}

var pythonVersion = '3.11'

resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      pythonVersion: pythonVersion
      linuxFxVersion: 'python|${pythonVersion}'
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: storageAccount.properties.primaryEndpoints.blob
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'WEBSITE_RUN_FROM_PACKAGE'
          value: '1'
        }
      ]
    }
  }
}
