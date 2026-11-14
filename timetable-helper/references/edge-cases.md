
# Timetable Helper - Edge Cases

## 1. Missing Batch

If the student asks for a timetable without specifying a batch, ask:

"Please provide your batch name so I can check the correct timetable."

Do not assume the batch.

## 2. Missing Day

If the student provides a batch but does not mention a day, ask which day they want.

## 3. Unknown Batch

If the batch is not present in the CSV, respond:

"I could not find this batch in the available timetable data. Please check the batch name."

## 4. Unknown Day

If the day is invalid or has no matching entries, explain that no timetable information was found.

## 5. Missing Subject

If a subject value is blank, do not create a subject name. Report that the subject information is unavailable.

## 6. Missing Faculty

If the faculty field is blank, display "Not available" rather than guessing a faculty name.

## 7. Conflicting User Information

If the student says that a class has been changed but the CSV still contains the old information, explain that the CSV does not confirm the change.

Do not silently update the timetable.

## 8. Adversarial Requests

If the student requests a fictional class or asks the agent to ignore the CSV:

- Reject the request to invent timetable information.
- Search the actual CSV.
- Show only matching entries.
- Explain when a requested class is not present.

## 9. CSV Access Failure

If the file is missing, corrupted, or inaccessible, do not generate a replacement timetable.

Explain that the information cannot currently be verified.
