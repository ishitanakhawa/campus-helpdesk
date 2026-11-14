
import csv
import json
import argparse
from pathlib import Path


def find_timetable(csv_file, batch, day):
    results = []

    csv_path = Path(csv_file)

    if not csv_path.is_file():
        raise FileNotFoundError(
            f"Timetable CSV not found: {csv_path}"
        )

    with csv_path.open(
        mode="r",
        encoding="utf-8-sig",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        required_columns = {
            "batch", "day", "start_time", "end_time",
            "course", "subject", "room", "faculty"
        }

        if not reader.fieldnames:
            raise ValueError("CSV file has no header.")

        if not required_columns.issubset(reader.fieldnames):
            raise ValueError(
                "CSV file is missing required columns."
            )

        for row in reader:
            if (
                row["batch"].strip().casefold() == batch.strip().casefold()
                and row["day"].strip().casefold() == day.strip().casefold()
            ):
                results.append({
                    "start_time": row["start_time"],
                    "end_time": row["end_time"],
                    "subject": row["subject"],
                    "room": row["room"],
                    "faculty": row["faculty"],
                    "course": row["course"]
                })

    results.sort(key=lambda item: item["start_time"])

    return results


def main():
    parser = argparse.ArgumentParser(
        description="Search the university timetable CSV."
    )

    parser.add_argument("--batch", required=True)
    parser.add_argument("--day", required=True)
    parser.add_argument(
        "--csv",
        default=str(
            Path(__file__).resolve().parent.parent
            / "data"
            / "timetable.csv"
        )
    )

    args = parser.parse_args()

    try:
        results = find_timetable(
            args.csv,
            args.batch,
            args.day
        )

        if results:
            output = {
                "status": "success",
                "batch": args.batch,
                "day": args.day,
                "classes": results
            }
        else:
            output = {
                "status": "no_match",
                "batch": args.batch,
                "day": args.day,
                "classes": [],
                "message": "No matching timetable entries found."
            }

        print(json.dumps(output, indent=4))

    except (FileNotFoundError, ValueError, OSError) as error:
        print(json.dumps({
            "status": "error",
            "message": str(error)
        }, indent=4))


if __name__ == "__main__":
    main()
