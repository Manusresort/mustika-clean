import { useState } from 'react'
import { useSearchParams, useNavigate, Link } from 'react-router-dom'
import { api, ClosureCreate } from '../api'
import './ClosureComposer.css'

const DECISION_TYPES = [
  'APPROVE',
  'REJECT',
  'DEFER',
  'REQUEST_CHANGES',
  'ESCALATE',
]

export default function ClosureComposer() {
  const [searchParams] = useSearchParams()
  const proposalId = searchParams.get('proposalId') || ''
  const runId = searchParams.get('runId') || ''
  const navigate = useNavigate()

  const [formData, setFormData] = useState<ClosureCreate>({
    proposal_id: proposalId,
    run_id: runId || undefined,
    decision_type: '',
    rationale: '',
    evidence_paths: [],
    sign_off: false,
  })

  const [evidencePath, setEvidencePath] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [success, setSuccess] = useState(false)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    
    if (!formData.decision_type) {
      setError('Decision type is required')
      return
    }
    
    if (formData.rationale.length < 10) {
      setError('Rationale must be at least 10 characters')
      return
    }
    
    if (!formData.sign_off) {
      setError('Sign-off is required')
      return
    }

    try {
      setLoading(true)
      setError(null)
      await api.createClosure(formData)
      setSuccess(true)
      setTimeout(() => {
        navigate('/inbox')
      }, 2000)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to create closure')
    } finally {
      setLoading(false)
    }
  }

  const addEvidencePath = () => {
    if (evidencePath.trim()) {
      setFormData({
        ...formData,
        evidence_paths: [...formData.evidence_paths, evidencePath.trim()],
      })
      setEvidencePath('')
    }
  }

  const removeEvidencePath = (index: number) => {
    setFormData({
      ...formData,
      evidence_paths: formData.evidence_paths.filter((_, i) => i !== index),
    })
  }

  if (success) {
    return (
      <div className="closure-composer">
        <div className="success-message">
          <h2>Closure created successfully!</h2>
          <p>Redirecting to inbox...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="closure-composer">
      <div className="closure-header">
        <Link to="/inbox" className="back-link">← Back to Inbox</Link>
        <h1>Create Closure</h1>
      </div>

      {error && (
        <div className="error">
          {error}
        </div>
      )}

      <form onSubmit={handleSubmit} className="closure-form">
        <div className="form-group">
          <label htmlFor="proposal_id">Proposal ID *</label>
          <input
            id="proposal_id"
            type="text"
            value={formData.proposal_id}
            onChange={(e) => setFormData({ ...formData, proposal_id: e.target.value })}
            required
            disabled={!!proposalId}
          />
        </div>

        <div className="form-group">
          <label htmlFor="run_id">Run ID (optional)</label>
          <input
            id="run_id"
            type="text"
            value={formData.run_id || ''}
            onChange={(e) => setFormData({ ...formData, run_id: e.target.value || undefined })}
            disabled={!!runId}
          />
        </div>

        <div className="form-group">
          <label htmlFor="decision_type">Decision Type *</label>
          <select
            id="decision_type"
            value={formData.decision_type}
            onChange={(e) => setFormData({ ...formData, decision_type: e.target.value })}
            required
          >
            <option value="">Select decision type</option>
            {DECISION_TYPES.map((type) => (
              <option key={type} value={type}>
                {type}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label htmlFor="rationale">Rationale * (min 10 characters)</label>
          <textarea
            id="rationale"
            value={formData.rationale}
            onChange={(e) => setFormData({ ...formData, rationale: e.target.value })}
            required
            minLength={10}
            rows={6}
            placeholder="Explain your decision..."
          />
          <div className="char-count">
            {formData.rationale.length} / 10 minimum
          </div>
        </div>

        <div className="form-group">
          <label>Evidence Paths</label>
          <div className="evidence-input">
            <input
              type="text"
              value={evidencePath}
              onChange={(e) => setEvidencePath(e.target.value)}
              placeholder="Path to evidence file..."
              onKeyPress={(e) => {
                if (e.key === 'Enter') {
                  e.preventDefault()
                  addEvidencePath()
                }
              }}
            />
            <button
              type="button"
              onClick={addEvidencePath}
              className="btn-add"
            >
              Add
            </button>
          </div>
          {formData.evidence_paths.length > 0 && (
            <ul className="evidence-list">
              {formData.evidence_paths.map((path, idx) => (
                <li key={idx}>
                  <code>{path}</code>
                  <button
                    type="button"
                    onClick={() => removeEvidencePath(idx)}
                    className="btn-remove"
                  >
                    Remove
                  </button>
                </li>
              ))}
            </ul>
          )}
        </div>

        <div className="form-group">
          <label className="checkbox-label">
            <input
              type="checkbox"
              checked={formData.sign_off}
              onChange={(e) => setFormData({ ...formData, sign_off: e.target.checked })}
              required
            />
            <span>I sign off on this decision *</span>
          </label>
        </div>

        <div className="form-actions">
          <button type="submit" disabled={loading} className="btn-primary">
            {loading ? 'Creating...' : 'Create Closure'}
          </button>
          <Link to="/inbox" className="btn-cancel">
            Cancel
          </Link>
        </div>
      </form>
    </div>
  )
}
