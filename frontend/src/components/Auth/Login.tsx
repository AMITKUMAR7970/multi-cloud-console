import React, { useState } from "react";
import { login, setAuthToken } from "../../services/api";

const Login: React.FC<{ onLogin: (token: string) => void }> = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [msg, setMsg] = useState("");

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const data = await login(email, password);
      setAuthToken(data.access_token);
      onLogin(data.access_token);
      setMsg("Success!");
    } catch {
      setMsg("Login failed");
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h3>Login</h3>
      <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
      <button type="submit">Login</button>
      <div>{msg}</div>
    </form>
  );
};

export default Login;