// API service stub 
import axios from "axios";

const API_BASE = process.env.REACT_APP_API_URL || "/api/v1";

export const setAuthToken = (token: string | null) => {
  if (token) axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  else delete axios.defaults.headers.common["Authorization"];
};

export const fetchAwsInstances = () =>
  axios.get(`${API_BASE}/cloud/aws/instances`).then(r => r.data);

export const fetchAzureVms = () =>
  axios.get(`${API_BASE}/cloud/azure/vms`).then(r => r.data);

export const fetchGcpInstances = () =>
  axios.get(`${API_BASE}/cloud/gcp/instances`).then(r => r.data);

export const startTerraformApply = (provider: string) =>
  axios.post(`${API_BASE}/cloud/terraform/apply?module=${provider}`).then(r => r.data);

export const fetchK8sClusters = () =>
  axios.get(`${API_BASE}/k8s/clusters`).then(r => r.data);

export const fetchMonitoringMetrics = (query: string) =>
  axios.get(`${API_BASE}/monitoring/prometheus/query?q=${encodeURIComponent(query)}`).then(r => r.data);

export const fetchNotifications = () =>
  axios.get(`${API_BASE}/notifications`).then(r => r.data);

export const fetchCloudCosts = () =>
  axios.get(`${API_BASE}/cost`).then(r => r.data);

export const login = (username: string, password: string) =>
  axios.post(`${API_BASE}/auth/login`, new URLSearchParams({ username, password })).then(r => r.data);