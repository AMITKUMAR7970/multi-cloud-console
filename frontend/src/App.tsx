import React, { useState } from "react";
import { setAuthToken } from "./services/api";
import { BrowserRouter as Router, Switch, Route, Link, Redirect } from "react-router-dom";
import DashboardPage from "./pages/DashboardPage";
import ProvisioningPage from "./pages/ProvisioningPage";
import MonitoringPage from "./pages/MonitoringPage";
import LogsPage from "./pages/LogsPage";
import LoginPage from "./pages/LoginPage";

const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(() => localStorage.getItem("token"));

  const handleLogin = (tok: string) => {
    setAuthToken(tok);
    setToken(tok);
    localStorage.setItem("token", tok);
  };

  const handleLogout = () => {
    setAuthToken(null);
    setToken(null);
    localStorage.removeItem("token");
  };

  return (
    <Router>
      <nav style={{ marginBottom: 16 }}>
        <Link to="/">Dashboard</Link> |{" "}
        <Link to="/provision">Provision</Link> |{" "}
        <Link to="/monitoring">Monitoring</Link> |{" "}
        <Link to="/logs">Logs</Link> |{" "}
        {token ? <button onClick={handleLogout}>Logout</button> : <Link to="/login">Login</Link>}
      </nav>
      <Switch>
        <Route exact path="/">
          {token ? <DashboardPage /> : <Redirect to="/login" />}
        </Route>
        <Route path="/provision">
          {token ? <ProvisioningPage /> : <Redirect to="/login" />}
        </Route>
        <Route path="/monitoring">
          {token ? <MonitoringPage /> : <Redirect to="/login" />}
        </Route>
        <Route path="/logs">
          {token ? <LogsPage /> : <Redirect to="/login" />}
        </Route>
        <Route path="/login">
          <LoginPage />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;