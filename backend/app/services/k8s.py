# Service logic for k8s 
from kubernetes import client, config
import os

def _get_kubeconfig(user):
    # For demo, load default; in prod, fetch from secret manager or user profile
    kubeconfig_path = os.getenv("KUBECONFIG", "~/.kube/config")
    config.load_kube_config(config_file=kubeconfig_path)

def list_clusters(user):
    # Assume a single cluster for demo; in prod, list from database or cloud
    _get_kubeconfig(user)
    # In real multi-cluster system, you would aggregate from cloud providers
    return [{"id": "default", "name": "default-cluster"}]

def get_cluster_info(cluster_id, user):
    _get_kubeconfig(user)
    v1 = client.CoreV1Api()
    nodes = v1.list_node().items
    pods = v1.list_pod_for_all_namespaces().items
    return {
        "node_count": len(nodes),
        "pod_count": len(pods),
        "nodes": [n.metadata.name for n in nodes],
        "pods": [p.metadata.name for p in pods]
    }