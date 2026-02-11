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
2) Install dependencies
pip install -r requirements.txt
3) Run migrations
python manage.py makemigrations
python manage.py migrate
4) Start server
python manage.py runserver
Open in browser:

Home: http://127.0.0.1:8000/

Tags: http://127.0.0.1:8000/tags/

Project Structure (important files)
todo_list/
  todo/                 # app
    models.py           # Task, Tag
    views.py            # List/CRUD views + toggle
    urls.py             # routes
    forms.py            # ModelForms
    templates/todo/     # base + pages
How to submit (Mate Academy)
Create a new public GitHub repo

Create dev branch and implement project there

Create Pull Request from dev → main

Attach screenshots of all pages directly into PR (NOT as links)

Submit PR link as solution

Screenshots
Add screenshots of:

Home page /

Tags page /tags/

Add/Update forms for Task and Tag

Delete confirmation pages


---

Якщо хочеш “максимальний флекс” для перевіряючого — скажи, і я додам у README:
- бейджі,  
- короткий demo section,  
- pre-commit/flake8 (опційно),  
- і команди для швидкого старту.
