/**
 * API client for Mustika Rasa Human UI
 */

const API_BASE = '/api'

export interface InboxItem {
  id: string
  kind: string
  severity: string
  source_type: 'run' | 'proposal'
  source_id: string
  reasons: string[]
  path: string
}

export interface InboxCounts {
  total: number
  by_kind: Record<string, number>
  by_status: Record<string, number>
}

export interface InboxResponse {
  generated_at: string
  counts: InboxCounts
  items: InboxItem[]
}

export interface Run {
  run_id: string
  manifest: any
  validator_report: string | null
  gates: any[]
  signals: any[]
  final_text: string | null
  review_notes: string | null
  outputs: {
    annotator_primary: any | null
    challenger_primary: any | null
    crew_provisional: any | null
  } | null
  warnings?: Array<{
    type: string
    file: string
    message: string
  }>
  output_files: Array<{ name: string; path: string; size: number }>
  log_files: Array<{ name: string; path: string; size: number }>
}

export interface Proposal {
  proposal_id: string
  proposal_md: string | null
  status: {
    status: string
    severity: string
  }
  gates: any[]
  required_closure: any
  review_pack_files: Array<{ name: string; path: string }>
  linked_runs: string[]
}

export interface Closure {
  closure_id: string
  created_at: string
  proposal_id: string
  source_run_id?: string
  decision_type: string
  rationale: string
  evidence_paths: string[]
  created_by: string
}

export interface ClosureCreate {
  proposal_id: string
  run_id?: string
  decision_type: string
  rationale: string
  evidence_paths: string[]
  sign_off: boolean
  created_by?: string
}

export const api = {
  async getInbox(): Promise<InboxResponse> {
    const response = await fetch(`${API_BASE}/inbox`)
    if (!response.ok) {
      let bodyText = ''
      try {
        bodyText = await response.text()
        if (bodyText.length > 2000) {
          bodyText = bodyText.substring(0, 2000)
        }
      } catch (e) {
        // Ignore errors reading body
      }
      throw new Error(`Failed to fetch inbox: ${response.status} ${response.statusText} - ${bodyText}`)
    }
    const payload = await response.json()
    const items: InboxItem[] = payload.items ?? []
    const counts: InboxCounts =
      payload.counts ?? {
        total: items.length,
        by_kind: {},
        by_status: {},
      }

    return {
      generated_at: payload.generated_at ?? '',
      counts,
      items,
    }
  },

  async getRun(runId: string): Promise<Run> {
    const response = await fetch(`${API_BASE}/runs/${runId}`)
    if (!response.ok) {
      throw new Error(`Failed to fetch run: ${response.statusText}`)
    }
    return response.json()
  },

  async getProposal(proposalId: string): Promise<Proposal> {
    const response = await fetch(`${API_BASE}/proposals/${proposalId}`)
    if (!response.ok) {
      throw new Error(`Failed to fetch proposal: ${response.statusText}`)
    }
    return response.json()
  },

  async getClosure(closureId: string): Promise<Closure> {
    const response = await fetch(`${API_BASE}/closures/${closureId}`)
    if (!response.ok) {
      throw new Error(`Failed to fetch closure: ${response.statusText}`)
    }
    return response.json()
  },

  async createClosure(closure: ClosureCreate): Promise<Closure> {
    const response = await fetch(`${API_BASE}/closures`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(closure),
    })
    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: response.statusText }))
      throw new Error(error.detail || `Failed to create closure: ${response.statusText}`)
    }
    return response.json()
  },

  async reindex(): Promise<{ status: string; result: any }> {
    const response = await fetch(`${API_BASE}/reindex`, {
      method: 'POST',
    })
    if (!response.ok) {
      throw new Error(`Failed to reindex: ${response.statusText}`)
    }
    return response.json()
  },
}
