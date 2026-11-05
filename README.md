# 🚀 Jira QA Agent V2 - Multi-Agent Architecture

## Overview

Jira QA Agent V2 evolves the V1 implementation from a function-based workflow into an Agent-based architecture.

The system retrieves Jira stories, extracts requirements, generates structured test cases, enriches them with AI-powered test design using Ollama, reviews coverage, assesses risk, and generates executive reports through multiple collaborating agents.

---

## V2 Architecture

```text
RequirementAgent
       ↓
Shared State
       ↓
TestDesignAgent
       ↓
Shared State
       ↓
ReviewAgent
       ↓
Shared State
       ↓
ReportAgent
```

---

## Agents

### RequirementAgent
- Connects to Jira
- Retrieves Jira story
- Extracts summary
- Extracts acceptance criteria
- Collects metadata
  - Priority
  - Status
  - Story Points
  - Labels

### TestDesignAgent
- Converts requirements into test scenarios
- Builds structured test cases
- Calls Ollama (Llama 3.2)
- Generates AI-powered test designs
- Updates state with generated test cases

### ReviewAgent
- Calculates requirement coverage
- Compares requirements vs generated tests
- Produces quality review
- Assigns risk level

### ReportAgent
- Generates Executive QA Report
- Summarizes metrics
- Produces management-friendly output

---

## Shared State Model

```python
state = {
    'story_id': '',
    'summary': '',
    'requirements': '',
    'priority': '',
    'status': '',
    'story_points': None,
    'labels': [],
    'test_cases': [],
    'coverage': {},
    'review': {},
    'report': ''
}
```

---

## Current Capabilities

- Jira Cloud Integration
- Jira Metadata Discovery
- Acceptance Criteria Extraction
- Structured Test Case Generation
- AI Test Design (Ollama)
- Coverage Analysis
- Risk Assessment
- Executive Reporting
- Shared-State Multi-Agent Workflow

---

## Sample Results

### Coverage

```text
Requirements : 5
Generated Tests : 5
Coverage : 100%
```

### Review

```text
Status : PASS
Risk : LOW
Recommendation : Requirement coverage is complete.
```

---

## Project Structure

```text
jira_qa_agent_v2
│
├── agents
│   ├── requirement_agent.py
│   ├── test_design_agent.py
│   ├── review_agent.py
│   └── report_agent.py
│
├── services
│   ├── jira_client.py
│   └── jira_fields.py
│
├── tools
├── outputs
├── config
└── main.py
```

---

## V2 Phase 1 Status

✅ RequirementAgent

✅ TestDesignAgent

✅ ReviewAgent

✅ ReportAgent

✅ Shared State Workflow

---

## Next Roadmap

### Phase 2
- CrewAI Integration
- Real Agent Roles
- Task-based execution

### Phase 3
- LangGraph StateGraph
- Directed Agent Workflow
- Advanced State Management

### Phase 4
- GitHub Actions CI/CD
- Automated Report Generation
- Artifact Publishing

### Phase 5
- MCP Integration
- Xray / Zephyr Integration
- Playwright Test Generation

---

## Author

Ravi Kumar

Associate Principal QE
QA Automation | Playwright | Python | GenAI | Agentic AI

---

## Version

Jira QA Agent V2 - Phase 1
