# Hybrid Cloud Manager: Setup Guide

## Prerequisites

- Docker & Docker Compose
- Python 3.9+
- Node.js 16+
- (Optional) Cloud CLI tools (AWS CLI, az, gcloud)
- (Optional) Access to AWS, Azure, GCP accounts for provisioning

## Quickstart (Dev)

1. **Clone the repo**
   ```sh
   git clone https://github.com/YOURORG/hybrid-cloud-manager.git
   cd hybrid-cloud-manager
   ```

2. **Set environment variables**  
   Copy `.env.example` to `.env` and fill in secrets for cloud and database access.

3. **Launch with Docker Compose**
   ```sh
   docker-compose up --build
   ```
   This starts backend, frontend, DB, Prometheus, Grafana, and Loki.

4. **Access the platform**
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:8000/docs](http://localhost:8000/docs)
   - Grafana: [http://localhost:3001](http://localhost:3001) (default admin/admin)
   - Prometheus: [http://localhost:9090](http://localhost:9090)

## Cloud Provisioning

- **Terraform**:  
  Edit variables in `infra/terraform/aws/variables.tf`, `azure/variables.tf`, `gcp/variables.tf`, then:
  ```sh
  cd infra/terraform/aws
  terraform init
  terraform apply
  ```

- **Ansible**:  
  Configure inventory/hosts, then run playbooks:
  ```sh
  ansible-playbook -i inventory infra/ansible/playbooks/install_docker.yml
  ```

- **Kubernetes/Helm**:  
  Install chart:
  ```sh
  helm upgrade --install hybrid-cloud-manager k8s/helm/app
  ```

## Monitoring

- Prometheus, Grafana, and Loki configs are in `monitoring/`.
- Connect Grafana to Prometheus and Loki datasources after first login.

---

## Notes

- For production, secure secrets, restrict CORS, and configure HTTPS.
- RBAC and user management require DB migration; see backend docs for details.

---