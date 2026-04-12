# End-of-day checklist (run before you mark a day as Done)

This repo is day-wise:

- You implement inside `dayX/lab1/` (starter workspace with TODOs).
- Some days have multiple labs: `dayX/lab1`, `dayX/lab2`, ...
- If you get stuck, reference solutions live in `dayX/solution/solution_labN/`.

## Checklist

1) Tracker
- Open `tracker.csv`
- Set today’s `Status` to:
  - `Done` only if all validation scenarios pass
  - otherwise `Blocked`
- Add short notes (what was hard, what you learned)

2) Code (`dayX/labN/`)
- Confirm you implemented all TODOs required by the day
- Run the day’s demo commands from `dayX/readme.md`

3) Tests
- Run day tests from repo root:
  - `python -m pytest -q dayX/lab1/tests`
- If no automated tests exist, run the manual validation scenarios from `dayX/readme.md`

4) Docs for other learners
- Ensure `dayX/readme.md` is accurate and runnable from a clean machine
- Ensure each lab has:
  - `problem_statement.md`
  - `guide.md`
  - `tests/`

6) Save + reset workspace
- Run:
  - `./scripts/submit_day.ps1 -Day dayX -Name <your_name>`
- Verify:
  - each `dayX/labN/` is reset to the starter code

7) Git hygiene
- `git status` is clean (no secrets, no `.env`, no `.venv`)
- Commit with a message like: `Day X - <topic>`
- Push to GitHub

Optional (recommended)
- Tag the day: `git tag day-X` then `git push --tags`
