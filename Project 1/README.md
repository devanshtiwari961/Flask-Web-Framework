# Project 1 — Flask Web Framework Basics

A hands-on introduction to Flask, covering routing, dynamic URLs, HTML templates, and form handling. This project is part of the Krish Naik Data Science Flask Web Framework course.

## Overview

Project 1 contains three progressive Flask applications that build on each other:

| File | Description |
|------|-------------|
| `app.py` | Basic Flask app with simple routes |
| `app1.py` | Dynamic URL building with variable rules |
| `main.py` | Full web app with HTML forms, Jinja2 templates, and GET/POST |

## Features

### `app.py` — Getting Started
- Creates a WSGI Flask application
- Defines routes using decorators (`@app.route`)
- Serves plain text responses at `/` and `/members`

### `app1.py` — Dynamic URLs
- Builds URLs dynamically using route variables
- Uses `<int:score>` to accept integer parameters
- Routes:
  - `/` — Welcome message
  - `/success/<score>` — Pass result with marks
  - `/fail/<score>` — Fail result with marks

### `main.py` — HTML Integration (Main Application)
- Renders HTML templates using the Jinja2 template engine
- Handles HTTP GET and POST requests
- Accepts student marks via a form and calculates the average
- Redirects users to pass/fail pages based on score (threshold: 50)

## Project Structure

```
Project 1/
├── app.py              # Basic routes demo
├── app1.py             # Dynamic URL demo
├── main.py             # Main app with forms and templates
├── requirements.txt    # Python dependencies
├── templates/
│   ├── index.html      # Marks entry form
│   └── result.html     # Result display page
└── static/
    ├── css/
    │   └── style.css   # Form styling
    └── script/
        └── script.js   # Client-side script
```

## Routes (`main.py`)

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Displays the marks entry form |
| `/submit` | POST, GET | Processes form data and redirects to result |
| `/success/<score>` | GET | Shows pass result with average score |
| `/fail/<score>` | GET | Shows fail result with average score |
| `/results/<marks>` | GET | Redirects to success or fail based on marks |

## How It Works

1. The user opens the home page and enters marks for four subjects: Science, Maths, C, and DS.
2. On submit, the app calculates the average score.
3. If the average is **50 or above**, the user is redirected to the success page.
4. If the average is **below 50**, the user is redirected to the fail page.
5. The result page displays the outcome (`PASS` / `FAIL`) and the average score.

## Jinja2 Template Syntax

`main.py` uses the Jinja2 template engine:

- `{{ expression }}` — Print output
- `{% statement %}` — Conditions and loops
- `{# comment #}` — Comments

## Prerequisites

- Python 3.7+
- pip

## Installation

1. Navigate to the project directory:

```bash
cd "Project 1"
```

2. (Recommended) Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the main application (recommended):

```bash
python main.py
```

Or try the simpler demos:

```bash
python app.py      # Basic routes
python app1.py     # Dynamic URLs
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

## Dependencies

- **Flask** — Web framework

## Learning Objectives

- Understand Flask routing and decorators
- Build dynamic URLs with variable rules
- Integrate HTML templates with Flask
- Handle GET and POST form submissions
- Use `redirect()` and `url_for()` for navigation
- Work with the Jinja2 template engine

## Notes

- Debug mode is enabled (`debug=True`) for development. Disable it in production.
- The pass/fail threshold is hardcoded at **50** in `main.py`.
