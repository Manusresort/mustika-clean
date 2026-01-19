import { useEffect, useState } from 'react'
import { Link, useSearchParams } from 'react-router-dom'
import { api, InboxItem } from '../api'
import './Inbox.css'

export default function Inbox() {
  const [items, setItems] = useState<InboxItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [searchParams, setSearchParams] = useSearchParams()
  const filter = searchParams.get('filter') || 'all'

  useEffect(() => {
    loadInbox()
  }, [])

  const loadInbox = async () => {
    try {
      setLoading(true)
      const data = await api.getInbox()
      setItems(data.items)
      setError(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load inbox')
    } finally {
      setLoading(false)
    }
  }

  const filteredItems = filter === 'all'
    ? items
    : items.filter(item => item.kind === filter)

  const getItemLink = (item: InboxItem) => {
    if (item.source_type === 'proposal') {
      return `/review/${item.source_id}`
    }
    if (item.source_type === 'run') {
      return `/runs/${item.source_id}`
    }
    return '#'
  }

  if (loading) {
    return <div className="inbox">Loading...</div>
  }

  if (error) {
    return (
      <div className="inbox">
        <div className="error">Error: {error}</div>
        <button onClick={loadInbox}>Retry</button>
      </div>
    )
  }

  return (
    <div className="inbox">
      <div className="inbox-header">
        <h1>Inbox</h1>
        <button onClick={loadInbox} className="btn-secondary">
          Refresh
        </button>
      </div>

      <div className="inbox-filters">
        <button
          className={filter === 'all' ? 'filter-active' : 'filter-btn'}
          onClick={() => setSearchParams({})}
        >
          All ({items.length})
        </button>
        <button
          className={filter === 'review_required' ? 'filter-active' : 'filter-btn'}
          onClick={() => setSearchParams({ filter: 'review_required' })}
        >
          Review ({items.filter(i => i.kind === 'review_required').length})
        </button>
        <button
          className={filter === 'gate' ? 'filter-active' : 'filter-btn'}
          onClick={() => setSearchParams({ filter: 'gate' })}
        >
          Gate ({items.filter(i => i.kind === 'gate').length})
        </button>
        <button
          className={filter === 'closure_needed' ? 'filter-active' : 'filter-btn'}
          onClick={() => setSearchParams({ filter: 'closure_needed' })}
        >
          Closure ({items.filter(i => i.kind === 'closure_needed').length})
        </button>
        <button
          className={filter === 'incident' ? 'filter-active' : 'filter-btn'}
          onClick={() => setSearchParams({ filter: 'incident' })}
        >
          Incidents ({items.filter(i => i.kind === 'incident').length})
        </button>
      </div>

      <div className="inbox-table">
        <table>
          <thead>
            <tr>
              <th>Severity</th>
              <th>Kind</th>
              <th>Source</th>
              <th>Reasons</th>
            </tr>
          </thead>
          <tbody>
            {filteredItems.length === 0 ? (
              <tr>
                <td colSpan={4} className="empty-state">
                  No items found
                </td>
              </tr>
            ) : (
              filteredItems.map((item) => (
                <tr key={item.id}>
                  <td>
                    <span className={`severity-badge severity-${item.severity}`}>
                      {item.severity}
                    </span>
                  </td>
                  <td>{item.kind}</td>
                  <td>
                    <Link to={getItemLink(item)} className="item-link">
                      {item.source_type}: {item.source_id}
                    </Link>
                  </td>
                  <td>{item.reasons.join(', ')}</td>
                </tr>
              ))
            )}
          </tbody>
        </table>
      </div>
    </div>
  )
}
