import React, { useState } from "react";
import Login from "../components/Auth/Login";

const LoginPage: React.FC = () => {
  const [token, setToken] = useState<string | null>(null);

  return (
    <div>
      <h1>Login</h1>
      {!token && <Login onLogin={setToken} />}
      {token && <div>Logged in! JWT: {token}</div>}
    </div>
  );
};

export default LoginPage;