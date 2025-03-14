# Kayzen Analytics MCP Server

This is a Model Context Protocol (MCP) server implementation for interacting with Kayzen Analytics API. It provides tools for accessing and analyzing Kayzen advertising campaign data through a standardized interface.

## Installation

```bash
# Install from npm
npm install @anthropic-ai/kayzen-mcp

# Or if you're using yarn
yarn add @anthropic-ai/kayzen-mcp
```

## Features

- **Authentication Management**: Automatic handling of authentication tokens with refresh mechanism
- **Report Management**: Tools for listing and retrieving report data
- **Data Analysis**: Built-in prompt for analyzing report results
- **Error Handling**: Robust error handling and reporting
- **TypeScript Support**: Full TypeScript implementation for type safety


## Prerequisites

- Node.js (v16 or higher)
- npm (v7 or higher)
- Kayzen API credentials

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file based on `.env.example` and fill in your Kayzen credentials:
```bash
cp .env.example .env
```

3. Configure your environment variables in `.env`:
```
KAYZEN_USERNAME=your_username
KAYZEN_PASSWORD=your_password
KAYZEN_BASIC_AUTH=your_basic_auth_token
KAYZEN_BASE_URL=https://api.kayzen.io/v1
```

## Development

To run the server in development mode with hot-reloading:

```bash
npm run dev
```

## Building

To compile the TypeScript code to JavaScript:

```bash
npm run build
```

The compiled code will be available in the `dist` directory.

## Running in Production

To run the compiled server:

```bash
npm start
```

## Available Tools

### 1. `list_reports`
Lists all available reports from Kayzen Analytics.

- **Parameters**: None
- **Returns**: JSON object containing list of available reports with their IDs and metadata

### 2. `get_report_results`
Retrieves results for a specific report.

- **Parameters**:
  - `report_id` (string, required): ID of the report to fetch
  - `start_date` (string, optional): Start date in YYYY-MM-DD format
  - `end_date` (string, optional): End date in YYYY-MM-DD format
- **Returns**: JSON object containing report data and metadata

## Available Prompts

### 1. `analyze_report_results`
Analyzes the results of a specific report and provides insights.

- **Parameters**:
  - `report_id` (string, required): ID of the report to analyze
- **Analysis includes**:
  - Performance metrics
  - Key trends
  - Areas for optimization
  - Unusual patterns or anomalies

## Error Handling

The server implements comprehensive error handling for:
- Authentication failures
- Invalid report IDs
- Network issues
- API rate limiting
- Invalid date ranges

## Project Structure

```
kayzen-mcp/
├── src/
│   ├── server.ts        # Main MCP server implementation
│   └── kayzen-client.ts # Kayzen API client implementation
├── dist/                # Compiled JavaScript code
├── package.json         # Project dependencies and scripts
└── tsconfig.json       # TypeScript configuration
```

## Dependencies

- `@modelcontextprotocol/sdk`: MCP server implementation
- `axios`: HTTP client for API requests
- `dotenv`: Environment variable management
- `zod`: Runtime type checking and validation
- `typescript`: Development dependency for type safety

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is proprietary and confidential. All rights reserved.
