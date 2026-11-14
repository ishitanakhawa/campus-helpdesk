# Campus Helpdesk Plugin

Campus Helpdesk is a Claude Code plugin designed to help students access campus-related information.

## Features

- Check timetable information using the timetable-helper skill.
- Use the check-timetable skill for timetable-related queries.
- Includes a custom slash command for timetable assistance.
- Includes a PreToolUse hook to protect files inside the data folder.
- Connects to the Campus Helpdesk MCP Server.
- Provides timetable and mock fee-status tools.
- Provides a hostel rules resource.

## MCP Server Setup

The plugin uses the MCP configuration in `.mcp.json` to start the Campus Helpdesk MCP Server.

The MCP server project is located in the `mcp-server` directory at the project root. It uses Python and `uv`.

## Installation

Install the plugin from the campus-helpdesk-marketplace:

    claude plugin install campus-helpdesk@campus-helpdesk-marketplace

## Testing

Validate the plugin using:

    claude plugin validate plugins/campus-helpdesk

The MCP server tools and hostel rules resource can be tested using MCP Inspector.

## Note

The timetable and fee records used by the MCP server are mock data for academic demonstration. They are not official university records.
