# TDEE & Macro Calculator

A full-stack web application that calculates Total Daily Energy Expenditure (TDEE) and personalized macro targets based on user inputs. Built with Python and Flask, converted from an original Tkinter desktop app.

## Features

- Calculates BMR using either the **Mifflin-St Jeor** formula (without body fat) or the **Katch-McArdle** formula (with body fat)
- Computes TDEE based on activity level
- Displays macro breakdowns for three goals: **Maintenance**, **Cut (−500 cal)**, and **Bulk (+500 cal)**
- Each goal includes three macro splits: Moderate Carb, Lower Carb, and Higher Carb
- Clean dark-themed UI with tabbed results display

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript (ES Modules)
- **Templating:** Jinja2

## Project Structure

```
tdee-web/
├── app.py              # Flask routes
├── calculator.py       # TDEE and macro logic (no UI dependencies)
├── static/
│   ├── styles.css      # Global styles
│   ├── script.js       # JS entry point
│   └── tabs.js         # Tab switching module
└── templates/
    ├── index.html      # Input form
    └── results.html    # Macro results display
```

## Running Locally

1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies
```bash
pip install flask
```

3. Start the Flask development server
```bash
python app.py
```

4. Open your browser and navigate to
```
http://127.0.0.1:5000
```

## Inputs

| Field | Description |
|---|---|
| Age | Years |
| Weight | Pounds |
| Gender | Male / Female |
| Height | 4ft 7in — 7ft 0in |
| Activity Level | Sedentary to Athlete |
| Body Fat % | Optional — enables Katch-McArdle formula |

## Screenshots

*Coming soon*
