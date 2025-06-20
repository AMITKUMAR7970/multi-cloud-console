# Service logic for azure 
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient
from app.services.secrets import get_azure_credentials

def list_azure_vms(user):
    creds = get_azure_credentials(user)
    credential = ClientSecretCredential(
        tenant_id=creds["tenant_id"],
        client_id=creds["client_id"],
        client_secret=creds["client_secret"]
    )
    compute_client = ComputeManagementClient(credential, creds["subscription_id"])
    vms = []
    for vm in compute_client.virtual_machines.list_all():
        vms.append({
            "name": vm.name,
            "location": vm.location,
            "type": vm.type
        })
    return vms