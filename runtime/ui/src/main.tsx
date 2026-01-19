import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

console.log("UI running at", window.location.origin)
console.log("API base", "/api (proxied by Vite to 127.0.0.1:8000)")

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)
