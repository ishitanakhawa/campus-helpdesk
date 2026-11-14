
from pathlib import Path

from mcp.server import MCPServer

# Create the MCP server
mcp = MCPServer("Campus Helpdesk MCP Server")


# Mock timetable data
MOCK_TIMETABLE = {
    ("CSE-JB-2", "Monday"): [
        {
            "start_time": "09:00",
            "end_time": "10:00",
            "subject": "Data Structures",
            "room": "Room 201",
            "faculty": "Prof. Sharma"
        },
        {
            "start_time": "10:15",
            "end_time": "11:15",
            "subject": "Database Management Systems",
            "room": "Room 203",
            "faculty": "Prof. Mehta"
        }
    ],
    ("CSE-JB-2", "Tuesday"): [
        {
            "start_time": "09:00",
            "end_time": "10:00",
            "subject": "Computer Networks",
            "room": "Room 202",
            "faculty": "Prof. Patel"
        }
    ]
}


# Mock fee data (no real student information)
MOCK_FEES = {
    "STU1001": {
        "student_id": "STU1001",
        "total_fees": 120000,
        "paid_amount": 90000,
        "pending_amount": 30000,
        "status": "Partially Paid"
    },
    "STU1002": {
        "student_id": "STU1002",
        "total_fees": 120000,
        "paid_amount": 120000,
        "pending_amount": 0,
        "status": "Fully Paid"
    }
}


@mcp.tool()
def get_timetable(batch: str, day: str) -> list[dict[str, str]]:
    """
    Retrieve the class timetable for a specified student batch and day.

    Args:
        batch: Student batch name, for example CSE-JB-2.
        day: Day of the week, for example Monday or Tuesday.

    Returns:
        A list containing class timings, subjects, classrooms and faculty.
        Raises an error if no matching mock timetable is available.
    """
    if not batch.strip():
        raise ValueError("Batch cannot be empty.")

    if not day.strip():
        raise ValueError("Day cannot be empty.")

    key = (batch.strip().upper(), day.strip().capitalize())

    if key not in MOCK_TIMETABLE:
        raise ValueError(
            f"No mock timetable found for batch '{batch}' on '{day}'."
        )

    return MOCK_TIMETABLE[key]


@mcp.tool()
def get_fee_status(student_id: str) -> dict[str, str | int]:
    """
    Retrieve mock fee payment information using a student ID.

    Args:
        student_id: Mock student ID, for example STU1001 or STU1002.

    Returns:
        Total fees, paid amount, pending amount and payment status.
        Raises an error if the mock student ID is not found.
    """
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty.")

    student_id = student_id.strip().upper()

    if student_id not in MOCK_FEES:
        raise ValueError(
            f"Student ID '{student_id}' was not found in mock fee records."
        )

    return MOCK_FEES[student_id]


@mcp.resource("campus://hostel/rules")
def hostel_rules() -> str:
    """
    Read the mock hostel rules and regulations document.
    """
    rules_file = (
        Path(__file__).parent / "resources" / "hostel_rules.md"
    )

    return rules_file.read_text(encoding="utf-8")


if __name__ == "__main__":
    # Run the MCP server over standard input/output
    mcp.run(transport="stdio")
