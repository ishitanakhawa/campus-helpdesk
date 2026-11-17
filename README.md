# Campus Helpdesk

**Campus Helpdesk** is an AI-assisted campus support project developed as part of the AI Tools and Prompt Engineering assignment.

The project demonstrates how AI Agent Skills, Claude Code plugins, Model Context Protocol (MCP) and Git Worktrees can be used together to build and manage a campus assistance system.

## 1. Project Objectives

- Help students access timetable information.
- Package reusable AI instructions into a Claude Code plugin.
- Provide campus information through MCP tools and resources.
- Protect important project data using a security hook.
- Understand parallel development using Git Worktrees.

## 2. Project Components

### A. Timetable Helper Skill

The `timetable-helper` Skill helps an AI agent answer timetable-related queries using an approved CSV file.

**Features:**
- Retrieves timetable information using batch and day.
- Provides subject, timing, classroom and faculty details.
- Handles missing or invalid inputs.
- Avoids generating imaginary timetable information.

### B. Campus Helpdesk Plugin

The `campus-helpdesk` plugin packages the timetable Skill and other campus assistance features.

**Components:**
- `plugin.json` – Plugin manifest.
- `timetable-helper` – Timetable Skill.
- `check-timetable.md` – Custom slash command.
- `protect_data.py` – Security hook.
- `.mcp.json` – MCP server configuration.

The security hook prevents direct Write/Edit operations inside the protected `data` folder.

### C. MCP Server

The Campus Helpdesk MCP Server is developed using Python and the official MCP Python SDK.

It provides two tools and one resource.

| Component | Purpose |
|---|---|
| `get_timetable` | Retrieves timetable information using batch and day. |
| `get_fee_status` | Retrieves mock fee payment information using student ID. |
| `campus://hostel/rules` | Provides the Hostel Rules resource. |

**Note:** The timetable and fee records are mock data. No real student database or payment system is connected.

## 3. Technologies Used

- Python 3.14.3
- Official MCP Python SDK
- Claude Code CLI
- Git and GitHub
- uv
- MCP Inspector
- JSON-RPC 2.0
- CSV and Markdown

## 4. Project Structure

```text
campus-helpdesk/
│
├── .claude-plugin/
│   └── marketplace.json
│
├── .github/
│   └── skills/
│       └── timetable-helper/
│           └── SKILL.md
│
├── plugins/
│   └── campus-helpdesk/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       ├── skills/
│       │   └── timetable-helper/
│       │       └── SKILL.md
│       ├── commands/
│       │   └── check-timetable.md
│       ├── hooks/
│       │   ├── hooks.json
│       │   └── scripts/
│       │       └── protect_data.py
│       ├── .mcp.json
│       └── README.md
│
├── mcp-server/
│   ├── src/
│   │   └── mcp_server/
│   │       ├── __init__.py
│   │       ├── server.py
│   │       └── resources/
│   │           └── hostel_rules.md
│   ├── evidence/
│   ├── pyproject.toml
│   ├── uv.lock
│   └── README.md
│
└── README.md
```

## 5. Installation and Setup

### Prerequisites

Install the following tools before working with the project:

- Python
- uv
- Git
- Claude Code CLI

### MCP Server Setup

Open the MCP server directory:

```bash
cd mcp-server
```

Install project dependencies:

```bash
uv sync
```

Check whether the server module imports successfully:

```bash
uv run python -c "from src.mcp_server.server import mcp; print('MCP server imported successfully')"
```

Launch MCP Inspector for testing:

```bash
uv run mcp dev src/mcp_server/server.py
```

### Plugin Installation

From the main project directory, register the local marketplace:

```bash
claude plugin marketplace add ./
```

Install the plugin:

```bash
claude plugin install campus-helpdesk@campus-helpdesk-marketplace
```

Verify the installation:

```bash
claude plugin list
```

## 6. Testing

The project components were tested separately.

| Test | Result |
|---|---|
| Timetable lookup | Tested |
| Invalid timetable query | Tested |
| Security hook protection | Tested |
| Plugin installation | Verified |
| Plugin component detection | Verified |
| MCP server import | Successful |
| `get_timetable` tool | Tested using MCP Inspector |
| `get_fee_status` tool | Tested using MCP Inspector |
| Hostel Rules resource | Tested using MCP Inspector |
| Invalid student ID | Error handled |
| JSON-RPC communication | Inspected |
| Git merge conflict | Successfully resolved |

## 7. Git Worktrees

Three separate worktrees were created to understand parallel development.

| Branch | Purpose |
|---|---|
| `feature/skill-tests` | Skill testing |
| `feature/mcp-server` | MCP server development |
| `bugfix/hook-path` | Hook path fixes and testing |

A merge conflict was deliberately created between the Skill Tests and MCP Server branches and resolved manually.

## 8. Important Security Considerations

- Use approved data sources instead of generating imaginary information.
- Validate tool inputs before processing them.
- Review tool descriptions and third-party integrations.
- Protect confidential student information.
- Restrict tools and hooks to the permissions they require.
- Review AI-generated changes before merging or executing them.

## 9. Limitations

- Timetable and fee information uses mock data.
- No real university database or payment system is connected.
- Live MCP tool execution through Claude Code could not be verified because account authentication was unavailable.
- The custom slash command's interactive execution was not verified.

## 10. Author

**Ishita Nakhawa**  
B.Tech – Computer Science and Engineering  
ITM Skills University
