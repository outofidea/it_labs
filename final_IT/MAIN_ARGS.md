# Gradebook CLI — Program Arguments

**Overview**

 This document describes the command-line arguments and subcommands exposed by `main.py` (Gradebook CLI). The CLI uses the `clypi` library and provides a `Gradebook` command with several subcommands for managing courses in the gradebook.


 **Invocation**
 - Typical invocation patterns (use the `uv` runner when available):
   - `uv run main.py <subcommand> [args...]` 
   - `python ./main.py <subcommand> [args...]` 
  
 **Commands & Arguments**
 - **AddCourse** (`add-course`): Add a specific course to the database.
   - Positional arguments (in order):
     - `CourseName` (string): Course name. Example: `"Introduction to Databases"`.
     - `CourseID` (string): Course code/ID. Example: `CS101`.
     - `NumCreds` (int): Number of credits. Example: `3`.
     - `Score` (int): Course score (numeric). Example: `85`.
     - `Semester` (int): Semester identifier/year. Example: `2025`.
   - Example:
     - `uv run gradebook add-course "Intro DB" CS101 3 85 2025`

 - **EditCourse** (`edit-course`): Edit fields of an existing course.
   - Positional argument:
     - `CourseID` (string): Course code/ID to edit.
   - Optional/interactive arguments (prompts or flags depending on `clypi` usage):
     - `CourseName` (string | None): New course name (prompt: "New course name ?").
     - `NumCreds` (int | None): New credits (prompt: "New course credits ?").
     - `Score` (float | None): New score (prompt: "New course score ?").
     - `Semester` (int | None): New semester (prompt: "New course semester ?").
   - Behavior:
     - If no edit arguments are provided, the command prints "No argument provided".
     - The command shows a side-by-side preview of OLD vs NEW values and asks for confirmation.
     - If confirmed, changes are saved via the DB; otherwise the operation is cancelled.
   - Example (non-interactive flags supported by `clypi` may vary):
     - `uv run gradebook edit-course CS101 --CourseName "DB Basics" --Score 90`
     - Or run `uv run gradebook edit-course CS101` and follow prompts.

 - **DeleteCourse** (`delete-course`): Delete a course by ID.
   - Positional argument:
     - `CourseId` (string): Course code to delete.
   - Behavior:
     - The command prompts for confirmation: "Really delete course with ID: <id>?".
     - If confirmed, attempts deletion and prints success/failure.
   - Example:
     - `uv run gradebook delete-course CS101`

 - **AddRandCourse** (`add-rand-course`): Add multiple randomly-named demo courses.
   - Positional argument:
     - `Num` (int): Number of fake courses to add.
   - Behavior:
     - Generates IDs like `AUH0000`, `AUH0001`, ... and inserts placeholder CourseInfo objects.
   - Example:
     - `uv run gradebook add-rand-course 5`

 - **ListCourses** (`list-courses`): List all courses.
   - No arguments.
   - Behavior:
     - Retrieves all courses and prints formatted boxed output for each entry.
   - Example:
     - `uv run gradebook list-courses`

 - **CalcGPA**: `(calc-gpa)`: Calculates total GPA of all courses in gradebook
   - No arguments
   - Behaviour: 
     - Calculates GPA and prints out result
   - Example: 
     - `uv run main.py calc-gpa`

 **Field Types & Models**
 - `CourseInfo` (from `db_management`) is the primary data structure for course records. Fields used in `main.py`:
   - `CourseName` — string
   - `CourseCreds` — int
   - `CourseScore` — float/int
   - `CourseSemester` — int

 **Interactive Prompts & Confirmations**
 - `EditCourse` uses prompts for optional fields when not supplied on the command-line.
 - `EditCourse` and `DeleteCourse` use `confirm(...)` to request yes/no confirmation from the user before committing changes.

**Subcommand usage (runtime help)**
The following usage blocks were captured by running `uv run python main.py <subcommand> --help` in this workspace. Use these as the exact runtime invocations and option names.

```
Usage: gradebook add-course [COURSENAME] [COURSEID] [NUMCREDS] [SCORE] [SEMESTER]

Arguments:
  [COURSENAME]  Course Name
  [COURSEID]    Course Code
  [NUMCREDS]    Number of credits
  [SCORE]       Score
  [SEMESTER]    Course Semester
```

```
Usage: gradebook list-courses
```

```
Usage: gradebook add-rand-course [NUM]

Arguments:
  [NUM]  Num courses to add
```

```
Usage: gradebook edit-course [COURSEID] [OPTIONS]

Arguments:
  [COURSEID]  Course Code

Options:
  --CourseName <COURSENAME>
  --NumCreds <NUMCREDS>
  --Score <SCORE>
  --Semester <SEMESTER>
```

```
Usage: gradebook delete-course [COURSEID]

Arguments:
  [COURSEID]  Course Code
```

 **Examples (quick copy-paste)**
 - Add a course:
   - `uv run gradebook add-course "Algorithms" CS201 4 92 2025`
 - Edit course interactively:
   - `uv run gradebook edit-course CS201`
 - Edit course non-interactively (flag syntax may depend on `clypi` runtime):
   - `uv run gradebook edit-course CS201 --CourseName "Advanced Algorithms" --Score 95`
 - List courses:
   - `uv run gradebook list-courses`
 - Delete a course (confirm when prompted):
   - `uv run gradebook delete-course CS201`
 - Add 3 random demo courses:
   - `uv run gradebook add-rand-course 3`

 **Notes & Caveats**
 - The exact command-line flag names and subcommand capitalization depend on `clypi`'s parsing and naming conventions. In this workspace the runtime usage shows kebab-cased subcommands: `add-course`, `list-courses`, `add-rand-course`, `edit-course`, `delete-course`.
 - If in doubt, run `uv run gradebook --help` or `uv run python main.py -- --help` to see parser-generated usage.
 - `CalcGPA` is not implemented; invoking it currently does nothing.
 - `EditCourse` reconstructs `CourseInfo` values and prints a preview before asking to confirm.

 **See Also**
 - Source code: `main.py` (at repository root).
 - Database layer: `db_management.py` (for `CourseInfo` schema and DB behavior).

 ---
 Generated by the project helper to document CLI arguments for `main.py` (updated after running `uv run` to capture exact subcommand names).
