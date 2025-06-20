import React from "react";
import JobLogStream from "../components/Logs/JobLogStream";

const LogsPage: React.FC = () => (
  <div>
    <h1>Job Logs</h1>
    {/* Example: Replace with real userId and jobId */}
    <JobLogStream userId="1" jobId={42} />
  </div>
);

export default LogsPage;