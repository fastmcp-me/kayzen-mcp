# Kayzen Analytics MCP Server

A Model Context Protocol (MCP) server implementation for interacting with Kayzen Analytics API. This package enables AI models to access and analyze Kayzen advertising campaign data through a standardized interface.

## Features

* **Automated Authentication**: Built-in token management with automatic refresh mechanism
* **Report Management**: Easy access to Kayzen analytics reports
* **Error Handling**: Comprehensive error handling for API interactions
* **TypeScript Support**: Full TypeScript implementation with type definitions
* **Environment Based Configuration**: Simple setup using environment variables

## Installation

```bash
npm install @feedmob-ai/kayzen-mcp
```

## Configuration

Create a `.env` file with your Kayzen credentials:

```bash
KAYZEN_USERNAME=your_username
KAYZEN_PASSWORD=your_password
KAYZEN_BASIC_AUTH=your_basic_auth_token
KAYZEN_BASE_URL=https://api.kayzen.io/v1  # Optional, defaults to this value
```

## Usage

### Basic Setup

```typescript
import { KayzenMCPServer } from '@feedmob-ai/kayzen-mcp';

const server = new KayzenMCPServer();
server.start();
```

## Available Tools

### 1. `list_reports`
Lists all available reports from Kayzen Analytics.

* **Inputs**: None
* **Returns**: Array of report objects containing:
  - `id`: Report identifier
  - `name`: Report name
  - `type`: Report type

```typescript
const reports = await server.tools.list_reports();
```

### 2. `get_report_results`
Retrieves results for a specific report.

* **Inputs**:
  - `report_id` (string, required): ID of the report to fetch
  - `start_date` (string, optional): Start date in YYYY-MM-DD format
  - `end_date` (string, optional): End date in YYYY-MM-DD format
* **Returns**: Report data and metadata

```typescript
const results = await server.tools.get_report_results({
  report_id: 'report_id',
  start_date: '2024-01-01',  // optional
  end_date: '2024-01-31'     // optional
});
```

### 3. `analyze_report_results` (Prompt)
Analyzes report results and provides insights.

* **Inputs**:
  - `report_id` (string): ID of the report to analyze
* **Analysis includes**:
  - Performance metrics
  - Key trends
  - Areas for optimization
  - Unusual patterns or anomalies


## Setup

### Usage with Claude Desktop
To use this with Claude Desktop, add the following to your `claude_desktop_config.json`:

### NPX

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": [
        "-y",
        "@feedmob-ai/kayzen-mcp"
      ],
      "env": {
        "KAYZEN_USERNAME": "username",
        "KAYZEN_PASSWORD": "pasword",
        "KAYZEN_BASIC_AUTH": "auth token"
      }
    }
  }
}
```


## Development

### Prerequisites

- Node.js (v16 or higher)
- npm (v7 or higher)
- Kayzen API credentials

### Scripts

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Start the server
npm start

# Development mode with hot-reload
npm run dev
```

## Project Structure

```
kayzen-mcp/
├── src/
│   ├── server.ts        # MCP server implementation
│   └── kayzen-client.ts # Kayzen API client
├── dist/               # Compiled JavaScript
└── package.json       # Project configuration
```

## Dependencies

Main dependencies:
- `@modelcontextprotocol/sdk`: ^1.7.0
- `axios`: ^1.8.3
- `dotenv`: ^16.4.7
- `zod`: ^3.24.2

## Error Handling

The server handles various error scenarios:
- Authentication failures
- Invalid API requests
- Network issues
- Token expiration and refresh
- Invalid parameters

## License

MIT License

## Author

FeedMob
