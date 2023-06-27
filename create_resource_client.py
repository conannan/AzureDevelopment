import get_config_file
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient


class CreateResourceClient:
    credential = AzureCliCredential()
    subscription_id = get_config_file.GetConfig.CONFIG["GlobalVariables"]["SUBSCRIPTION_ID"]
    resource_client = ResourceManagementClient(credential, subscription_id)


if __name__ == '__main__':
    client = CreateResourceClient.resource_client
    rg_result = client.resource_groups.create_or_update(
        "PythonAzureExample-rg", {"location": "centralus"}
    )
    print(
        f"Provisioned resource group {rg_result.name} in \
            the {rg_result.location} region"
    )
