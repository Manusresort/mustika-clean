import { useEffect, useState } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { api, Proposal } from '../api'
import './ReviewPackViewer.css'

export default function ReviewPackViewer() {
  const { proposalId } = useParams<{ proposalId: string }>()
  const [proposal, setProposal] = useState<Proposal | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const navigate = useNavigate()

  useEffect(() => {
    if (proposalId) {
      loadProposal(proposalId)
    }
  }, [proposalId])

  const loadProposal = async (id: string) => {
    try {
      setLoading(true)
      const data = await api.getProposal(id)
      setProposal(data)
      setError(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load proposal')
    } finally {
      setLoading(false)
    }
  }

  const handleApprove = () => {
    if (proposalId) {
      navigate(`/closure/new?proposalId=${proposalId}`)
    }
  }

  if (loading) {
    return <div className="review-pack-viewer">Loading...</div>
  }

  if (error) {
    return (
      <div className="review-pack-viewer">
        <div className="error">Error: {error}</div>
        <Link to="/inbox">Back to Inbox</Link>
      </div>
    )
  }

  if (!proposal) {
    return <div className="review-pack-viewer">Proposal not found</div>
  }

  return (
    <div className="review-pack-viewer">
      <div className="review-header">
        <Link to="/inbox" className="back-link">← Back to Inbox</Link>
        <h1>Review: {proposal.proposal_id}</h1>
        <div className={`status-badge status-${proposal.status.status}`}>
          {proposal.status.status}
        </div>
      </div>

      <div className="review-layout">
        <div className="review-left">
          <section className="review-section">
            <h2>Proposal Content</h2>
            <div className="proposal-content">
              <pre>{proposal.proposal_md || '(No content)'}</pre>
            </div>
          </section>
        </div>

        <div className="review-right">
          {proposal.gates && proposal.gates.length > 0 && (
            <section className="review-section">
              <h2>Gates ({proposal.gates.length})</h2>
              <div className="gates-list">
                {proposal.gates.map((gate, idx) => (
                  <div key={idx} className={`gate-item ${gate.blocking ? 'gate-blocking' : ''}`}>
                    <div className="gate-header">
                      <span className="gate-type">{gate.type || 'Unknown'}</span>
                      {gate.blocking && <span className="gate-badge">Blocking</span>}
                    </div>
                    <div className="gate-details">
                      {JSON.stringify(gate, null, 2)}
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}

          {proposal.required_closure && (
            <section className="review-section">
              <h2>Required Closure</h2>
              <div className="required-closure">
                <pre>{JSON.stringify(proposal.required_closure, null, 2)}</pre>
              </div>
            </section>
          )}

          {proposal.linked_runs && proposal.linked_runs.length > 0 && (
            <section className="review-section">
              <h2>Linked Runs</h2>
              <ul className="linked-runs">
                {proposal.linked_runs.map((runId, idx) => (
                  <li key={idx}>
                    <Link to={`/runs/${runId}`}>{runId}</Link>
                  </li>
                ))}
              </ul>
            </section>
          )}
        </div>
      </div>

      <div className="review-actions">
        <button onClick={handleApprove} className="btn-primary">
          Approve → Create Closure
        </button>
        <button className="btn-secondary">Request Changes</button>
        <button className="btn-danger">Reject</button>
      </div>
    </div>
  )
}
