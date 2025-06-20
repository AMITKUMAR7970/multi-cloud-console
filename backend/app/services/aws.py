# Service logic for aws 
import boto3
from app.services.secrets import get_aws_credentials

def list_ec2_instances(user):
    creds = get_aws_credentials(user)
    ec2 = boto3.client(
        "ec2",
        aws_access_key_id=creds["access_key"],
        aws_secret_access_key=creds["secret_key"],
        region_name=creds["region"]
    )
    reservations = ec2.describe_instances()["Reservations"]
    instances = []
    for r in reservations:
        for i in r["Instances"]:
            instances.append({
                "id": i["InstanceId"],
                "type": i["InstanceType"],
                "state": i["State"]["Name"],
                "name": next((t["Value"] for t in i.get("Tags", []) if t["Key"] == "Name"), ""),
                "public_ip": i.get("PublicIpAddress")
            })
    return instances