import React from "react";
import CloudOverview from "../components/Dashboard/CloudOverview";
import ClusterList from "../components/K8s/ClusterList";
import NotificationList from "../components/Notifications/NotificationList";

const DashboardPage: React.FC = () => (
  <div>
    <h1>Hybrid Cloud Manager Dashboard</h1>
    <CloudOverview />
    <ClusterList />
    <NotificationList />
  </div>
);

export default DashboardPage;