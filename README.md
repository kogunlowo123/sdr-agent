# SDR Agent

[![CI](https://github.com/kogunlowo123/sdr-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/sdr-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Sales | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Sales Development Representative AI agent that qualifies inbound leads, books meetings, handles objections, follows up with prospects, and maintains CRM hygiene for the sales development pipeline.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `qualify_inbound` | Qualify an inbound lead and determine next action |
| `book_meeting` | Book a meeting between a qualified prospect and an AE |
| `handle_objection` | Generate objection handling response for a common sales objection |
| `follow_up` | Generate and schedule follow-up message for a prospect |
| `update_crm` | Update CRM with interaction notes and next steps |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/sdr/execute` | Execute primary action |
| `POST` | `/api/v1/sdr/analyze` | Run analysis |
| `GET` | `/api/v1/sdr/metrics` | Get metrics |
| `PUT` | `/api/v1/sdr/configure` | Configure settings |
| `POST` | `/api/v1/sdr/report` | Generate report |

## Features

- Sdr
- Analytics
- Automation

## Integrations

- Salesforce
- Hubspot
- Outreach
- Apollo
- Linkedin Sales Navigator

## Architecture

```
sdr-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── sdr_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**CRM + Sales Engagement + LLM**

---

Built as part of the Enterprise AI Agent Platform.
