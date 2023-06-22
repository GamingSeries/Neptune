import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Login from './Login';  // Ensure the path is correct based on your file structure

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        {/* Add more routes as necessary */}
      </Routes>
    </Router>
  );
}

export default App;
