from contextlib import asynccontextmanager
from typing import AsyncIterator, Optional
from datetime import datetime, timedelta
import json

from mcp.server.fastmcp import FastMCP, Context
from kayzen_client import KayzenClient

@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[dict]:
    """Initialize Kayzen client"""
    client = KayzenClient()
    try:
        yield {"client": client}
    finally:
        pass

# Create MCP server with lifespan
mcp = FastMCP(
    "Kayzen Analytics",
    dependencies=["httpx", "python-dotenv", "pydantic"],
    lifespan=app_lifespan
)

@mcp.tool()
async def create_report(
    ctx: Context,
    report_type: str,
    start_date: str,
    end_date: str,
    dimensions: list[str],
    metrics: list[str]
) -> str:
    """
    Create a new Kayzen report

    Args:
        report_type: Type of report (e.g. 'campaign', 'creative')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        dimensions: List of dimensions to include
        metrics: List of metrics to include
    """
    client: KayzenClient = ctx.request_context.lifespan_context["client"]

    try:
        result = await client.create_report(
            report_type=report_type,
            start_date=start_date,
            end_date=end_date,
            dimensions=dimensions,
            metrics=metrics
        )
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error creating report: {str(e)}"

@mcp.tool()
async def get_report_status(ctx: Context, report_id: str) -> str:
    """
    Get the status of a Kayzen report

    Args:
        report_id: ID of the report to check
    """
    client: KayzenClient = ctx.request_context.lifespan_context["client"]

    try:
        result = await client.get_report_status(report_id)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error getting report status: {str(e)}"

@mcp.tool()
async def get_report_results(ctx: Context, report_id: str) -> str:
    """
    Get the results of a completed Kayzen report

    Args:
        report_id: ID of the report to fetch results for
    """
    client: KayzenClient = ctx.request_context.lifespan_context["client"]

    try:
        result = await client.get_report_results(report_id)
        return json.dumps(result, indent=2)
    except Exception as e:
        return f"Error getting report results: {str(e)}"

@mcp.prompt()
def create_campaign_report() -> str:
    """Template for creating a campaign performance report"""
    return """Please help me create a campaign performance report with the following specifications:

1. Report type: campaign
2. Time period: Last 7 days
3. Dimensions: campaign_id, campaign_name
4. Metrics: impressions, clicks, spend, ctr, cpc

Please use the create_report tool with these parameters."""

@mcp.prompt()
def analyze_report_results() -> str:
    """Template for analyzing report results"""
    return """I have a report with ID {report_id}. Please:

1. Check the report status
2. If it's complete, fetch and analyze the results
3. Provide insights about:
   - Top performing campaigns
   - Areas for optimization
   - Unusual patterns or anomalies"""

if __name__ == "__main__":
    mcp.run()
