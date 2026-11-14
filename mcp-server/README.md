# Campus Helpdesk MCP Server

## 1. Project Overview

The Campus Helpdesk MCP Server is a minimal Model Context Protocol (MCP) server developed using Python and the official MCP Python SDK.

It helps students access mock campus information through MCP tools and resources.

The server communicates over standard input/output (stdio).

**Important:** This project uses mock data only. It does not connect to any real student database or payment system.

## 2. Technologies Used

- Python 3.14
- Official MCP Python SDK
- uv package manager
- MCP Inspector
- JSON-RPC 2.0
- Markdown

## 3. Project Structure

```text
mcp-server/
├── src/
│   └── mcp_server/
│       ├── __init__.py
│       ├── server.py
│       └── resources/
│           └── hostel_rules.md
├── .venv/
├── README.md
├── pyproject.toml
└── uv.lock
```

## 4. MCP Server Features

The server exposes two tools and one resource.

### Tool 1: get_timetable

**Purpose:** Retrieves the class timetable for a specified batch and day.

**Input Parameters:**
- batch (string): Student batch name.
- day (string): Day of the week.

**Example Input:**

```json
{
  "batch": "CSE-JB-2",
  "day": "Monday"
}
```

**Output:** Class timings, subject names, classrooms and faculty details.

### Tool 2: get_fee_status

**Purpose:** Retrieves mock fee payment information using a student ID.

**Input Parameter:**
- student_id (string): Mock student ID.

**Example Input:**

```json
{
  "student_id": "STU1001"
}
```

**Mock Student Records:**

| Student ID | Total Fees | Paid | Pending | Status |
|---|---:|---:|---:|---|
| STU1001 | 120000 | 90000 | 30000 | Partially Paid |
| STU1002 | 120000 | 120000 | 0 | Fully Paid |

### Resource: Hostel Rules

**Resource URI:** `campus://hostel/rules`

**Purpose:** Provides the mock hostel rules and regulations document.

The resource contains information about:
- Entry and exit timings
- Visitors
- Cleanliness
- Safety and security
- Discipline

## 5. Installation and Setup

### Prerequisites

- Python 3.11 or newer
- uv package manager
- Node.js and npm for MCP Inspector

### Step 1: Navigate to the project folder

```bash
cd mcp-server
```

### Step 2: Install dependencies

```bash
uv sync
```

### Step 3: Run the MCP server

```bash
uv run python src/mcp_server/server.py
```

The server runs over stdio and waits for communication from an MCP client.

**Note:** Running the server directly in a terminal may appear to produce no output because stdio is used for MCP communication.

## 6. Testing with MCP Inspector

The server was tested using MCP Inspector.

Run the following command:

```bash
uv run mcp dev src/mcp_server/server.py
```

The MCP Inspector interface opens in a browser.

The following tests were performed:

1. Server connection and initialization.
2. Verification of both registered tools.
3. Successful execution of `get_timetable`.
4. Successful execution of `get_fee_status`.
5. Reading the Hostel Rules resource.
6. Invalid student ID failure test using `STU9999`.

## 7. JSON-RPC Communication

The MCP communication was verified through the following JSON-RPC methods:

- `initialize`: Establishes communication and negotiates capabilities between the client and server.
- `tools/list`: Retrieves available tools and their input schemas.
- `tools/call`: Executes a selected tool and returns its result.

The server successfully announced its support for tools, resources and prompts during initialization.

## 8. Failure Handling

An invalid student ID, `STU9999`, was provided to the `get_fee_status` tool.

The server returned a tool error response with:

```json
{
  "isError": true
}
```

This demonstrates that invalid mock student IDs are not treated as successful requests.

## 9. Security Considerations

- Only mock data is used.
- Tool inputs are validated before processing.
- Invalid student IDs and unavailable timetable records generate errors.
- Tool descriptions are kept task-specific.
- Third-party tool descriptions should be reviewed to reduce prompt injection and tool poisoning risks.

## 10. Conclusion

The Campus Helpdesk MCP Server was successfully developed using the official Python MCP SDK.

It exposes two functional tools, `get_timetable` and `get_fee_status`, and one Hostel Rules resource.

The server was tested using MCP Inspector. Successful tool calls, resource reading, JSON-RPC communication and an invalid-input failure case were verified.

This project demonstrates how MCP allows AI applications to discover and use external tools and resources through a standardized communication protocol.