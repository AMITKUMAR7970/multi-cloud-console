# Hybrid Cloud Manager

**Hybrid Cloud Manager** is a robust, modular platform for unified provisioning, management, and monitoring across AWS, Azure, and GCP. It streamlines cloud resource operations, Kubernetes automation, job orchestration, cost visibility, and observability—all accessible from a modern web dashboard.

---

## 🚀 Key Features

- **Multi-Cloud Resource Management:** Provision, list, and manage VMs and resources across AWS, Azure, and GCP from a single UI
- **Kubernetes Automation:** Register, deploy, and monitor multiple clusters and workloads
- **Job Orchestration:** Run Terraform, Ansible, or K8s jobs with real-time log streaming (WebSockets)
- **Cost Analytics:** View and compare cloud spend and trends across providers
- **Monitoring & Logging:** Integrated Prometheus, Grafana, Loki, and Alertmanager for metrics, dashboards, and logs
- **Notifications:** In-app and email alerts for job outcomes, incidents, and system health
- **RBAC & Authentication:** JWT-secured endpoints; built-in user and role management
- **Extensible Architecture:** Modular backend, pluggable cloud/provider adapters, customizable frontend

---

## 🏗️ Tech Stack

- **Backend:** Python, FastAPI, PostgreSQL, WebSockets, JWT Auth
- **Frontend:** React, TypeScript, Axios, React Router
- **Infra as Code:** Terraform (multi-cloud), Ansible, Helm, Docker Compose
- **Observability:** Prometheus, Grafana, Loki, Alertmanager

---

## 📦 Directory Structure

```
├── backend/                  # FastAPI backend (modular, async, RBAC)
│   ├── app/
│   │   ├── api/              # API routers (cloud, k8s, cost, monitoring, auth, etc.)
│   │   ├── models/           # SQLAlchemy/Pydantic models
│   │   ├── services/         # Cloud, K8s, monitoring logic
│   │   ├── utils/            # Utilities (logging, validators)
│   │   └── core/             # Settings, database, security
├── frontend/                 # React + TypeScript dashboard UI
│   ├── src/
│   │   ├── components/       # Dashboard, ProvisioningWizard, K8s, Monitoring, Logs, Notifications, Auth
│   │   ├── pages/            # Page wrappers for routing
│   │   └── services/         # API and websocket connectors
├── infra/
│   ├── terraform/            # AWS, Azure, GCP modules for network/vm
│   ├── ansible/roles/        # Docker, k8s, monitoring install roles
│   └── k8s/helm/             # App, Prometheus, Grafana charts
├── monitoring/               # Prometheus, Loki, Alertmanager configs; Grafana dashboards
├── docs/                     # Architecture, setup, usage guides
├── .github/workflows/        # CI/CD for backend & frontend
└── README.md
```

---

## 🧑‍💻 Getting Started

### 1. **Clone and Setup**

```sh
git clone https://github.com/YOURORG/hybrid-cloud-manager.git
cd hybrid-cloud-manager
cp .env.example .env
# Fill in DB/cloud secrets in .env, backend/app/core/config.py, and frontend/.env if needed
```

### 2. **Run Locally (Dev)**

```sh
docker-compose up --build
```
- **Frontend:** http://localhost:3000  
- **Backend API & Docs:** http://localhost:8000/docs  
- **Grafana:** http://localhost:3001 (admin/admin)  
- **Prometheus:** http://localhost:9090  

### 3. **Provision Cloud Resources**

- Edit `infra/terraform/{aws,azure,gcp}/variables.tf` for your account & region
- Run:
  ```sh
  cd infra/terraform/aws
  terraform init && terraform apply
  ```

### 4. **Kubernetes & Helm**

- Register clusters and deploy apps/monitoring from the frontend or with:
  ```sh
  helm upgrade --install hybrid-cloud-manager k8s/helm/app
  ```

### 5. **Monitoring/Logging**

- Import example dashboards from `monitoring/grafana-dashboards/` into Grafana
- Connect Grafana to Prometheus and Loki datasources as needed

---

## 🔄 What You Should Change for Your Own Use

**1. Secrets & Credentials**
- Replace all example secrets in `.env`, backend config, and cloud providers with your own
- For production, use a secrets manager (AWS Secrets Manager, Vault, etc.)

**2. Email & Notification Settings**
- Update `monitoring/alertmanager.yml` with your own email/SMTP credentials for alerts

**3. Domain & SSL**
- Configure CORS/allowed hosts and HTTPS for production
- Set up your DNS and TLS certificates

**4. User & RBAC Policies**
- Seed your own users and adjust roles in the backend database
- Review and adjust RBAC enforcement in `app/services/auth.py` and related files

**5. Cloud Regions & Project IDs**
- Update Terraform/Ansible `variables.tf` and inventory files for your accounts, regions, and permissions

**6. Branding & UI**
- Change logos, colors, and titles in `frontend/src/components/` and `public/`

**7. Extend/Customize**
- Add cloud providers: implement new adapters in `backend/app/services/`
- Add more dashboard panels: create and import Grafana JSON dashboards
- Add custom API endpoints or UI features as your workflows require

**8. Logging & Security**
- Harden backend (rate limiting, input validation)
- Set up external log aggregation and audit logging

---

## 📝 Documentation

- [Architecture Guide](docs/architecture.md)
- [Setup Instructions](docs/setup.md)
- [Usage Guide](docs/usage.md)
- [CI/CD Workflows](.github/workflows/)
- [Sample Grafana Dashboards](monitoring/grafana-dashboards/)

---

## 🧪 Testing & CI/CD

- Backend: run `pytest` in `backend/`
- Frontend: run `npm test` in `frontend/`
- Automated workflows in `.github/workflows/` for PRs and pushes

---

## 💡 Contribution

- Fork, branch, and submit PRs!
- Open issues for bugs, ideas, or integrations
- Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) if available

---

## 🛡️ License

MIT (or your preferred license)

---

## 🙏 Acknowledgements

Built with FastAPI, React, Terraform, Ansible, Helm, Prometheus, Grafana, and the open source community.

---

> **Note:**  
> This project is a starting point for scalable, multi-cloud, Kubernetes, and monitoring automation.  
> Review all configuration, secrets, and RBAC/ACL policies before deploying for real-world use.
