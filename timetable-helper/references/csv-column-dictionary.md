
# CSV Column Dictionary

The timetable is stored in data/timetable.csv.

Each row represents one scheduled class.

## Column Definitions

| Column | Description | Example |
|---|---|---|
| batch | Student batch identifier | CSE-JB-2 |
| day | Day of the scheduled class | Monday |
| start_time | Starting time of the class | 09:00 |
| end_time | Ending time of the class | 10:00 |
| course | Academic course | BTech CSE |
| subject | Name of the subject | Data Structures |
| room | Classroom or laboratory | Room 201 |
| faculty | Faculty member conducting the class | Prof. Sharma |

## Data Rules

1. Batch names must match the CSV entries.
2. Days are written using their full names.
3. Time values use the 24-hour HH:MM format.
4. Every row represents one class.
5. A blank value must not be replaced with an assumed value.
6. The CSV is the only approved source for timetable answers.
7. Do not add information based on general assumptions.
