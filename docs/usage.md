# Hybrid Cloud Manager Usage Guide

## 1. Cloud Resource Management

- **View Cloud Resources**  
  Go to the dashboard to view all AWS EC2, Azure VM, and GCP Compute instances. Resource counts and details auto-refresh.

- **Provision Cloud Resources**
  1. Use the Provisioning Wizard in the dashboard.
  2. Select provider (AWS/Azure/GCP), region, instance size, and OS.
  3. Submit – the backend triggers a Terraform job and streams logs live.

- **Multi-cloud Inventory**
  - See all discovered resources across clouds in a unified view.
  - Filter and search by cloud, state, or resource name.

## 2. Kubernetes Operations

- **View Clusters and Nodes**
  - See all registered clusters.
  - Click for details: node count, pod count, health, resource usage.

- **Deploy to K8s**
  - Use the “Deploy” function to launch Helm charts (including your app, Prometheus, Grafana).
  - Monitor deployment logs in real-time.

## 3. Monitoring & Logging

- **Metrics**
  - Access the Monitoring section for CPU, memory, pod, and node stats.
  - Grafana dashboards are linked for deep-dive visualization.

- **Logs**
  - Access live job logs via the Logs panel (WebSocket-powered).
  - Loki integration allows full-text search and alerting.

## 4. Cost & Notifications

- **Cloud Cost Analytics**
  - See estimated monthly spend per cloud.
  - Prometheus metrics power Grafana cost panels.

- **Notifications**
  - Receive in-app alerts for job completions, failures, or cloud changes.
  - All alerts are stored and accessible via the Notifications panel.

## 5. RBAC & Security

- **User Management**
  - Admins can add/remove users, set roles (admin, user, viewer).
  - RBAC enforced for all API endpoints.

- **Secrets Handling**
  - All cloud credentials are stored securely (e.g., AWS Secrets Manager).
  - Never hardcode secrets in code.

## 6. Advanced Features

- **API Access**
  - Use `/api/v1/*` endpoints for automation (see [API docs](../backend/app/main.py)).
  - JWT-based authentication required for all endpoints.

- **Extend Providers**
  - Add new cloud providers by implementing new adapters under `backend/app/services/`.

- **Add Dashboards**
  - Import new JSON dashboards into Grafana via the web UI or API.

---

## Troubleshooting

- **Terraform/Ansible errors:** Review logs in the Logs panel or backend logs.
- **Grafana/Loki/Prometheus:** Restart affected containers and verify config files.
- **Cloud API limits:** Ensure your cloud accounts have proper quotas and credentials.