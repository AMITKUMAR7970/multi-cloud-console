import React, { useState } from "react";
import { fetchMonitoringMetrics } from "../../services/api";

const PrometheusQuery: React.FC = () => {
  const [query, setQuery] = useState("up");
  const [result, setResult] = useState<any>(null);

  const handleQuery = async () => {
    const data = await fetchMonitoringMetrics(query);
    setResult(data);
  };

  return (
    <div>
      <h4>Prometheus Query</h4>
      <input value={query} onChange={e => setQuery(e.target.value)} />
      <button onClick={handleQuery}>Run</button>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
};

export default PrometheusQuery;