import React, { useEffect, useState } from "react";
import { fetchK8sClusters } from "../../services/api";

const ClusterList: React.FC = () => {
  const [clusters, setClusters] = useState<any[]>([]);

  useEffect(() => {
    fetchK8sClusters().then(setClusters);
  }, []);

  return (
    <div>
      <h3>Kubernetes Clusters</h3>
      <ul>
        {clusters.map(c => (
          <li key={c.id || c.name}>
            {c.name} (ID: {c.id || "default"})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ClusterList;