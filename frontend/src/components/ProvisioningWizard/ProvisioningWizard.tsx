import React, { useState } from "react";
import { startTerraformApply } from "../../services/api";

const ProvisioningWizard: React.FC = () => {
  const [provider, setProvider] = useState("aws");
  const [logs, setLogs] = useState<string>("");

  const handleProvision = async () => {
    setLogs("Provisioning started...\n");
    try {
      const res = await startTerraformApply(provider);
      setLogs(l => l + "Provisioning complete: " + JSON.stringify(res) + "\n");
    } catch (e: any) {
      setLogs(l => l + "Provisioning failed: " + (e.message || e.toString()) + "\n");
    }
  };

  return (
    <div>
      <h3>Provision Cloud Resource</h3>
      <label>
        Provider:
        <select value={provider} onChange={e => setProvider(e.target.value)}>
          <option value="aws">AWS</option>
          <option value="azure">Azure</option>
          <option value="gcp">GCP</option>
        </select>
      </label>
      <button onClick={handleProvision}>Provision</button>
      <pre style={{ background: "#222", color: "#eee", padding: 12 }}>{logs}</pre>
    </div>
  );
};

export default ProvisioningWizard;