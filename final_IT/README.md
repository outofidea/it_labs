# Sam Nhat Lam - AUH14961 - Final IT Portfolio

## Installation of Gradebook CLI

### Prerequisites: 
- Astral [uv](https://docs.astral.sh/uv/#installation) Python Package Manager
- Python 3 or higher

### Package Installation:
```
uv sync
```
or:
 ```
 pip install pickledb clypi
 ```

### Usage
```
uv run main.py
```

or

```
python3 ./main.py
```

### Examples
- Add a course:
  - `python main.py AddCourse "Algorithms" CS201 4 92 2025`
- Edit course interactively:
  - `python main.py EditCourse CS201`
- Edit course non-interactively (flag syntax may depend on `clypi` runtime):
  - `python main.py EditCourse CS201 --CourseName "Advanced Algorithms" --Score 95`
- List courses:
  - `python main.py ListCourses`
- Delete a course (confirm when prompted):
  - `python main.py DeleteCourse CS201`
- Add 3 random demo courses:
  - `python main.py AddRandCourse 3`

See [Program Arguments](./MAIN_ARGS.md)

## CLI Usage (runtime)

When using the workspace `uv` runner the CLI exposes a `gradebook` command with kebab-cased subcommands. Below are the exact runtime invocations captured in this environment.

- List of subcommands:
  - `add-course` — Add a course
  - `list-courses` — List all courses
  - `add-rand-course` — Add multiple demo courses
  - `edit-course` — Edit an existing course
  - `delete-course` — Delete a course

Examples (using `uv`):

```
uv run python main.py add-course "Algorithms" CS201 4 92 2025
uv run python main.py list-courses
uv run python main.py add-rand-course 3
uv run python main.py edit-course CS201 --CourseName "Advanced Algorithms" --Score 95
uv run python main.py delete-course CS201
```

For full argument/option details for each subcommand see [MAIN_ARGS.md](./MAIN_ARGS.md).
<details>
  <summary> epic easter egg </summary>

![./image.png](./resource/image.png) 

</details>
