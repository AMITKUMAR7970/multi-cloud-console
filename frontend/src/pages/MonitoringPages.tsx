import React from "react";
import PrometheusQuery from "../components/Monitoring/PrometheusQuery";

const MonitoringPage: React.FC = () => (
  <div>
    <h1>Monitoring</h1>
    <PrometheusQuery />
  </div>
);

export default MonitoringPage;