import boto3
import os
import json

def get_aws_credentials(user):
    secret_name = os.environ.get("AWS_SECRET_NAME", "hybridcloud/aws")
    region = os.environ.get("AWS_REGION", "us-east-1")
    client = boto3.client("secretsmanager", region_name=region)
    secret = client.get_secret_value(SecretId=secret_name)
    creds = json.loads(secret["SecretString"])
    return {
        "access_key": creds["AWS_ACCESS_KEY_ID"],
        "secret_key": creds["AWS_SECRET_ACCESS_KEY"],
        "region": creds["AWS_REGION"]
    }

def get_azure_credentials(user):
    secret_name = os.environ.get("AZURE_SECRET_NAME", "hybridcloud/azure")
    region = os.environ.get("AZURE_REGION", "eastus")
    client = boto3.client("secretsmanager", region_name=region)
    secret = client.get_secret_value(SecretId=secret_name)
    creds = json.loads(secret["SecretString"])
    return {
        "client_id": creds["AZURE_CLIENT_ID"],
        "client_secret": creds["AZURE_CLIENT_SECRET"],
        "tenant_id": creds["AZURE_TENANT_ID"],
        "subscription_id": creds["AZURE_SUBSCRIPTION_ID"]
    }

def get_gcp_credentials(user):
    secret_name = os.environ.get("GCP_SECRET_NAME", "hybridcloud/gcp")
    region = os.environ.get("GCP_REGION", "us-central1")
    client = boto3.client("secretsmanager", region_name=region)
    secret = client.get_secret_value(SecretId=secret_name)
    creds = json.loads(secret["SecretString"])
    return {
        "service_account_info": creds["GCP_SERVICE_ACCOUNT_JSON"],
        "project_id": creds["GCP_PROJECT_ID"]
    }