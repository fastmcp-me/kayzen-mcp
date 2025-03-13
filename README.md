# Kayzen MCP Server

An MCP server that integrates with the Kayzen API to fetch and analyze advertising campaign data.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your Kayzen API credentials:
```bash
KAYZEN_API_KEY=your_api_key
KAYZEN_API_SECRET=your_api_secret
```

## Features

### Tools

- `create_report`: Create a new Kayzen report with custom dimensions and metrics
- `get_report_status`: Check the status of a report
- `get_report_results`: Fetch results of a completed report

### Prompts

- `create_campaign_report`: Template for creating a campaign performance report
- `analyze_report_results`: Template for analyzing report results

## Usage

1. Start the server:
```bash
python server.py
```

2. Install in Claude Desktop:
```bash
mcp install server.py
```

3. Test with MCP Inspector:
```bash
mcp dev server.py
```

## Example Usage

1. Create a campaign report:
```python
result = await create_report(
    report_type="campaign",
    start_date="2024-01-01",
    end_date="2024-01-31",
    dimensions=["campaign_id", "campaign_name"],
    metrics=["impressions", "clicks", "spend"]
)
```

2. Check report status:
```python
status = await get_report_status("report_id_here")
```

3. Get report results:
```python
results = await get_report_results("report_id_here")
```
