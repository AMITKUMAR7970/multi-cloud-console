# Hybrid Cloud Manager: Architecture

## Overview

Hybrid Cloud Manager is a full-stack platform for multi-cloud resource management, Kubernetes automation, job orchestration, cost monitoring, and real-time log streaming. It integrates:

- **Backend**: FastAPI (Python), real-time WebSocket logs, secure secret management, modular cloud adapters (AWS/Azure/GCP), RBAC, monitoring, and cost endpoints.
- **Frontend**: React + TypeScript dashboard with live job logs, cloud resource management, and monitoring.
- **Infrastructure**: Terraform (multi-cloud), Ansible (provisioning), Helm (K8s app/monitoring deployment).
- **Observability**: Prometheus, Grafana, Loki, Alertmanager.

## Key Components

### Backend (FastAPI)
- Modular API endpoints: `/cloud`, `/k8s`, `/cost`, `/monitoring`, `/notifications`
- Real-time log streaming via WebSockets
- Secure cloud credentials (AWS Secrets Manager)
- Async job orchestration (Terraform, Ansible, K8s)
- Role-based access control (RBAC)
- Monitoring and notification endpoints

### Frontend (React)
- Cloud resource dashboards (AWS, Azure, GCP)
- Job log streaming (WebSocket)
- Provisioning wizard
- Kubernetes cluster and workload view
- Monitoring dashboards (Prometheus/Grafana)
- Notifications and cost analytics

### Infrastructure
- **Terraform**: Provisions cloud resources (VMs, networks) in AWS, Azure, GCP using modular code.
- **Ansible**: Automates software install (Docker, K8s, monitoring agents).
- **Helm**: Deploys platform and observability stack to Kubernetes.

### Monitoring & Logging
- **Prometheus**: Metrics collection
- **Grafana**: Dashboards
- **Loki**: Log aggregation
- **Alertmanager**: Alerts/notifications

## Data Flow

1. **User** (frontend) triggers a cloud or K8s operation.
2. **Backend** launches async job (Terraform/Ansible/K8s), logs progress.
3. **Frontend** streams job logs via WebSocket.
4. **Prometheus** scrapes backend, cloud, and K8s metrics.
5. **Grafana** visualizes metrics/cost/alerts.
6. **Loki** aggregates logs, searchable in Grafana.

---