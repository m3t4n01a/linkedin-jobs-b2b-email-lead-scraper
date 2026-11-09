# LinkedIn & Google Jobs Scraper + Automatic B2B Company Email Enricher

[![Run on Apify Store](https://img.shields.io/badge/Apify_Store-Run_Actor-00C853?style=for-the-badge&logo=apify)](https://apify.com/willowy_catamaran_fco/google-linkedin-jobs-scraper)
[![MCP Compatible](https://img.shields.io/badge/MCP-AI_Agent_Ready-7C3AED?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/google-linkedin-jobs-scraper/api)
[![n8n & Clay Ready](https://img.shields.io/badge/Integrations-n8n_%7C_Clay_%7C_Make-FF6D5A?style=for-the-badge)](https://apify.com/willowy_catamaran_fco/google-linkedin-jobs-scraper)

Extract active job postings and automatically resolve each hiring company's domain, verified B2B contact emails, and internal tech stack in a single run.

---

## Why Growth Teams & AI Agents Use This Actor
- **Flat, Pre-Validated JSON Output:** Zero nested arrays - maps directly into **Clay.com columns**, **n8n HTTP Request nodes**, **Make.com**, **HubSpot**, and **Airtable**.
- **High-Concurrency Async Engine:** Powered by concurrent worker pools and TLS browser impersonation (`curl_cffi`) with low 256MB-512MB RAM footprint.
- **MCP & Autonomous Agent Ready:** Runs under `LIMITED_PERMISSIONS` with predictable Pay-Per-Event pricing so Claude, Cursor, LangChain, and CrewAI agents can call it autonomously.

---

## Quick Start: 1-Click API Call (n8n / Clay / cURL)

Use the synchronous endpoint below in **Clay (HTTP API enrichment)** or **n8n (HTTP Request node)** to run the extraction and receive the JSON array in a single request:

```bash
curl -X POST "https://api.apify.com/v2/acts/willowy_catamaran_fco~google-linkedin-jobs-scraper/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
  "query": "AI Engineer",
  "location": "United Kingdom",
  "maxItems": 25
}'
```

---

## Sample Input
```json
{
  "query": "AI Engineer",
  "location": "United Kingdom",
  "maxItems": 25
}
```

## Real Output Sample
```json
{
  "jobTitle": "Artificial Intelligence Engineer",
  "companyName": "Searchability",
  "companyDomain": "searchability.com",
  "primaryEmail": "info@searchability.com",
  "techStackCsv": "Microsoft 365, Google Workspace, Cloudflare, Google Analytics 4, WordPress",
  "location": "Manchester Area, United Kingdom"
}
```

---

## Connect to Claude Desktop / Cursor via Apify MCP
Add this Actor to your AI agent toolset using the official Apify MCP Server:
```json
{
  "mcpServers": {
    "apify-b2b-tools": {
      "command": "npx",
      "args": [
        "-y",
        "@apify/actors-mcp-server",
        "--actors",
        "willowy_catamaran_fco/google-linkedin-jobs-scraper"
      ],
      "env": {
        "APIFY_TOKEN": "YOUR_APIFY_TOKEN"
      }
    }
  }
}
```

## Keywords & Integrations
`linkedin-jobs-scraper, b2b-leads, hiring-intent-signals, outbound-automation, n8n, clay, apify-actor, mcp-server`
