# Service logic for gcp 
from google.oauth2 import service_account
from googleapiclient.discovery import build
from app.services.secrets import get_gcp_credentials

def list_gcp_instances(user):
    creds = get_gcp_credentials(user)
    credentials = service_account.Credentials.from_service_account_info(creds["service_account_info"])
    project = creds["project_id"]
    service = build('compute', 'v1', credentials=credentials)
    result = service.instances().aggregatedList(project=project).execute()
    instances = []
    for zone, data in result['items'].items():
        for inst in data.get('instances', []):
            instances.append({
                "name": inst["name"],
                "zone": zone,
                "status": inst["status"],
                "type": inst["machineType"]
            })
    return instances