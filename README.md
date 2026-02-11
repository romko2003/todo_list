# Todo List (Django)

A simple Django Todo List application with Tasks and Tags.

## Features
- Home page `/`:
  - Sidebar with navigation to Home and Tags (on every page)
  - List of tasks ordered:
    1) Not done → Done
    2) Newest → Oldest
  - Display task content, created time, optional deadline, tags
  - Add task button
  - Update/Delete links for each task
  - Complete/Undo button to toggle status

- Tags page `/tags/`:
  - List of tags in a table (name + update/delete)
  - Add tag button
  - CRUD for tags

## Tech Stack
- Python 3.x
- Django 5.x
- SQLite (default)

## Setup & Run

### 1) Create and activate venv
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
# Windows: venv\Scripts\activate
