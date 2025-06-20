import React, { useEffect, useState } from "react";
import { fetchAwsInstances, fetchAzureVms, fetchGcpInstances } from "../../services/api";

const CloudOverview: React.FC = () => {
  const [aws, setAws] = useState<any[]>([]);
  const [azure, setAzure] = useState<any[]>([]);
  const [gcp, setGcp] = useState<any[]>([]);

  useEffect(() => {
    fetchAwsInstances().then(setAws);
    fetchAzureVms().then(setAzure);
    fetchGcpInstances().then(setGcp);
  }, []);

  return (
    <div>
      <h2>Cloud Overview</h2>
      <h3>AWS</h3>
      <ul>{aws.map(i => <li key={i.id}>{i.name || i.id} ({i.state})</li>)}</ul>
      <h3>Azure</h3>
      <ul>{azure.map(i => <li key={i.name}>{i.name} ({i.type})</li>)}</ul>
      <h3>GCP</h3>
      <ul>{gcp.map(i => <li key={i.name}>{i.name} ({i.status})</li>)}</ul>
    </div>
  );
};

export default CloudOverview;