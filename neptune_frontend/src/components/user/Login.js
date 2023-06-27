import React, { useState } from 'react';
import axios from 'axios';
import './login.css';  

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const data = { email, password };
      console.log(data); //This will log your data to the console
      const response = await axios.post('http://localhost:8000/user/jwt/create/', data);
      console.log(response.data);
    } catch (error) {
      console.error(error);
    }
  };
  return (
    <div className="container">
      <form onSubmit={handleSubmit} className="login-form">
        <div className="field">
          <div className="email">
            <label htmlFor="email">Email</label>
          </div>
          <div className="field-box form-input">
            <input id="email" type="email" value={email} onChange={e => setEmail(e.target.value)} required />
          </div>
        </div>
        <div className="field">
          <div className="password">
            <label htmlFor="password">Password</label>
          </div>
          <div className="form-input">
            <input id="password" type="password" value={password} onChange={e => setPassword(e.target.value)} required />
          </div>
        </div>
        <div className="submit">
          <button className="submit-btn" type="submit">Login</button>
        </div>
      </form>
    </div>
  );
}

export default Login;
