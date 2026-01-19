import { BrowserRouter, Routes, Route, Link } from 'react-router-dom'
import Dashboard from './components/Dashboard'
import Inbox from './components/Inbox'
import ReviewPackViewer from './components/ReviewPackViewer'
import ClosureComposer from './components/ClosureComposer'
import RunDetail from './components/RunDetail'
import './App.css'

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <nav className="navbar">
          <div className="nav-container">
            <Link to="/" className="nav-logo">
              Mustika Rasa
            </Link>
            <div className="nav-links">
              <Link to="/">Dashboard</Link>
              <Link to="/inbox">Inbox</Link>
            </div>
          </div>
        </nav>
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/inbox" element={<Inbox />} />
            <Route path="/review/:proposalId" element={<ReviewPackViewer />} />
            <Route path="/closure/new" element={<ClosureComposer />} />
            <Route path="/runs/:runId" element={<RunDetail />} />
          </Routes>
        </main>
      </div>
    </BrowserRouter>
  )
}

export default App
