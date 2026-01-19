import { useEffect, useState } from 'react'
import { useParams, Link } from 'react-router-dom'
import { api, Run } from '../api'
import './RunDetail.css'

export default function RunDetail() {
  const { runId } = useParams<{ runId: string }>()
  const [run, setRun] = useState<Run | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [showWarnings, setShowWarnings] = useState(false)

  useEffect(() => {
    if (runId) {
      loadRun(runId)
    }
  }, [runId])

  const loadRun = async (id: string) => {
    try {
      setLoading(true)
      const data = await api.getRun(id)
      setRun(data)
      setError(null)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Failed to load run')
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="run-detail">Loading...</div>
  }

  if (error) {
    return (
      <div className="run-detail">
        <div className="error">Error: {error}</div>
        <Link to="/inbox">Back to Inbox</Link>
      </div>
    )
  }

  if (!run) {
    return <div className="run-detail">Run not found</div>
  }

  return (
    <div className="run-detail">
      <div className="run-detail-header">
        <Link to="/inbox" className="back-link">← Back to Inbox</Link>
        <h1>Run: {run.run_id}</h1>
      </div>

      {run.warnings && run.warnings.length > 0 && (
        <section className="run-section">
          <h2>
            <button 
              onClick={() => setShowWarnings(!showWarnings)}
              className="warnings-toggle"
              style={{ background: 'none', border: 'none', cursor: 'pointer', padding: 0, textAlign: 'left' }}
            >
              Warnings ({run.warnings.length}) {showWarnings ? '▼' : '▶'}
            </button>
          </h2>
          {showWarnings && (
            <div className="warnings-list">
              {run.warnings.map((warning, idx) => (
                <div key={idx} className="warning-item">
                  <div className="warning-header">
                    <span className="warning-type">{warning.type}</span>
                    {warning.file && <code className="warning-file">{warning.file}</code>}
                  </div>
                  {warning.message && (
                    <div className="warning-message">{warning.message}</div>
                  )}
                </div>
              ))}
            </div>
          )}
        </section>
      )}

      <div className="run-sections">
        <section className="run-section">
          <h2>Manifest</h2>
          <pre className="code-block">
            {JSON.stringify(run.manifest, null, 2)}
          </pre>
        </section>

        <section className="run-section">
          <h2>Final Text</h2>
          {run.final_text ? (
            <pre className="code-block">{run.final_text}</pre>
          ) : run.outputs?.crew_provisional ? (
            <div>
              <p className="empty-state">No final text for this run. Showing crew_provisional output:</p>
              <pre className="code-block">
                {JSON.stringify(run.outputs.crew_provisional, null, 2)}
              </pre>
            </div>
          ) : (
            <p className="empty-state">No final text for this run</p>
          )}
        </section>

        <section className="run-section">
          <h2>Review Notes</h2>
          {run.review_notes ? (
            <pre className="code-block">{run.review_notes}</pre>
          ) : (
            <p className="empty-state">No review notes</p>
          )}
        </section>

        <section className="run-section">
          <h2>Validator Report</h2>
          {run.validator_report ? (
            <pre className="code-block">{run.validator_report}</pre>
          ) : (
            <p className="empty-state">No validator report</p>
          )}
        </section>

        {run.outputs && (
          <section className="run-section">
            <h2>Outputs</h2>
            {run.outputs.annotator_primary && (
              <div className="output-item">
                <h3>Annotator Primary</h3>
                <pre className="code-block">
                  {JSON.stringify(run.outputs.annotator_primary, null, 2)}
                </pre>
              </div>
            )}
            {run.outputs.challenger_primary && (
              <div className="output-item">
                <h3>Challenger Primary</h3>
                <pre className="code-block">
                  {JSON.stringify(run.outputs.challenger_primary, null, 2)}
                </pre>
              </div>
            )}
            {run.outputs.crew_provisional && (
              <div className="output-item">
                <h3>Crew Provisional</h3>
                <pre className="code-block">
                  {JSON.stringify(run.outputs.crew_provisional, null, 2)}
                </pre>
              </div>
            )}
          </section>
        )}

        {run.gates && run.gates.length > 0 && (
          <section className="run-section">
            <h2>Gates ({run.gates.length})</h2>
            <div className="gates-list">
              {run.gates.map((gate, idx) => (
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

        {run.signals && run.signals.length > 0 && (
          <section className="run-section">
            <h2>Signals ({run.signals.length})</h2>
            <div className="signals-list">
              {run.signals.map((signal, idx) => (
                <div key={idx} className="signal-item">
                  <div className="signal-header">
                    <span className="signal-type">{signal.type || 'Unknown'}</span>
                    <span className={`severity-badge severity-${signal.severity || 'info'}`}>
                      {signal.severity || 'info'}
                    </span>
                  </div>
                  <div className="signal-details">
                    {JSON.stringify(signal, null, 2)}
                  </div>
                </div>
              ))}
            </div>
          </section>
        )}

        {run.output_files && run.output_files.length > 0 && (
          <section className="run-section">
            <h2>Output Files ({run.output_files.length})</h2>
            <ul className="file-list">
              {run.output_files.map((file, idx) => (
                <li key={idx}>
                  <code>{file.name}</code> ({file.size} bytes)
                </li>
              ))}
            </ul>
          </section>
        )}

        {run.log_files && run.log_files.length > 0 && (
          <section className="run-section">
            <h2>Log Files ({run.log_files.length})</h2>
            <ul className="file-list">
              {run.log_files.map((file, idx) => (
                <li key={idx}>
                  <code>{file.name}</code> ({file.size} bytes)
                </li>
              ))}
            </ul>
          </section>
        )}
      </div>
    </div>
  )
}
