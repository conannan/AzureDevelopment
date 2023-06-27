import create_resource_client
import get_config_file

class ResourceGroup:
    client = create_resource_client.CreateResourceClient.resource_client


    @staticmethod
    def create_or_update_resource_group(rg_name, json_config):
        rg_result = ResourceGroup.client.resource_groups.create_or_update(rg_name, json_config)
        return rg_result

    @staticmethod
    def delete_resource_group(rg_name):
        rg_result = ResourceGroup.client.resource_groups.begin_delete(rg_name)
        return rg_result

    @staticmethod
    def delete_resources(rg_name, resource_type, resource_name=None):
        rg_result = ResourceGroup.client.resources.begin_delete_by_id(get_config_file.GetConfig.CONFIG["GlobalVariables"]["SUBSCRIPTION_ID"], rg_name, resource_type)
        return rg_result

if __name__ == '__main__':
    name = "test_function"
    json = {"location": "centralus", "tags":{"department":"QA"}}
    test_result = ResourceGroup.create_or_update_resource_group(name, json)
    print(
        f"Provisioned resource group {test_result.name} in \
            the {test_result.location} region"
    )
    test_result = ResourceGroup.delete_resource_group(name)
    print(test_result.name)