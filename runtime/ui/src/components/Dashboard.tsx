import { useEffect, useState } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { api, InboxResponse, InboxItem } from '../api'
import './Dashboard.css'

export default function Dashboard() {
  const [inbox, setInbox] = useState<InboxResponse | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const navigate = useNavigate()

  const getItemLink = (item: InboxItem) => {
    if (item.source_type === 'proposal') {
      return `/review/${item.source_id}`
    }
    if (item.source_type === 'run') {
      return `/runs/${item.source_id}`
    }
    return '#'
  }

  useEffect(() => {
    loadDashboard()
  }, [])

  const loadDashboard = async () => {
    try {
      setLoading(true)
      const data = await api.getInbox()
      setInbox(data)
      setError(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load dashboard')
    } finally {
      setLoading(false)
    }
  }

  const handleReindex = async () => {
    try {
      await api.reindex()
      await loadDashboard()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to reindex')
    }
  }

  if (loading) {
    return <div className="dashboard">Loading...</div>
  }

  if (error) {
    return (
      <div className="dashboard">
        <div className="error">Error: {error}</div>
        <button onClick={loadDashboard}>Retry</button>
      </div>
    )
  }

  if (!inbox) {
    return <div className="dashboard">No data</div>
  }

  return (
    <div className="dashboard">
      <div className="dashboard-header">
        <h1>Dashboard</h1>
        <button onClick={handleReindex} className="btn-secondary">
          Reindex
        </button>
      </div>

      <div className="dashboard-widgets">
        <div className="widget">
          <h2>Inbox Summary</h2>
          <div className="counters">
            <Link to="/inbox?filter=review_required" className="counter-card">
              <div className="counter-value">{inbox.items.filter(i => i.kind === 'review_required').length}</div>
              <div className="counter-label">Review Required</div>
            </Link>
            <Link to="/inbox?filter=gate" className="counter-card">
              <div className="counter-value">{inbox.items.filter(i => i.kind === 'gate').length}</div>
              <div className="counter-label">Gate Triggered</div>
            </Link>
            <Link to="/inbox?filter=closure_needed" className="counter-card">
              <div className="counter-value">{inbox.items.filter(i => i.kind === 'closure_needed').length}</div>
              <div className="counter-label">Closure Needed</div>
            </Link>
            <Link to="/inbox?filter=incident" className="counter-card">
              <div className="counter-value">{inbox.items.filter(i => i.kind === 'incident').length}</div>
              <div className="counter-label">Incidents</div>
            </Link>
          </div>
        </div>

        <div className="widget">
          <h2>Recent Activity</h2>
          <div className="activity-list">
            {inbox.items.slice(0, 5).map((item) => (
              <div key={item.id} className="activity-item" onClick={() => navigate(getItemLink(item))} style={{ cursor: 'pointer' }}>
                <span className={`severity-badge severity-${item.severity}`}>
                  {item.severity}
                </span>
                <span className="activity-title">{item.kind}: {item.source_type} {item.source_id}</span>
                <span className="activity-action">{item.reasons.join(', ')}</span>
              </div>
            ))}
            {inbox.items.length === 0 && (
              <div className="empty-state">No items in inbox</div>
            )}
          </div>
          <Link to="/inbox" className="view-all-link">
            View all items →
          </Link>
        </div>
      </div>
    </div>
  )
}
