# OrangeHRM Playwright Python Automation

End-to-end UI automation framework for the OrangeHRM application using **Playwright, Python, Pytest, Page Object Model (POM), and Allure Reporting**.

## Tech Stack

* Python
* Playwright
* Pytest
* Page Object Model
* Allure Report
* Python-dotenv
* Git
* GitHub

## Framework Architecture

```text
Tests
  │
  ▼
Page Objects
  │
  ▼
Base Page
  │
  ▼
Playwright
  │
  ▼
OrangeHRM
```

## Project Structure

```text
OrangeHRMAutomation/
│
├── config/
├── pages/
├── tests/
├── utils/
├── allure-results/
├── allure-report/
├── screenshots/
├── logs/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Automated Modules

### Login

* Valid login
* Invalid username
* Invalid password
* Invalid credentials
* Empty username
* Empty password
* Logout

### Dashboard

* Dashboard validation
* PIM navigation
* Leave navigation
* Recruitment navigation
* Admin navigation

### PIM

* Open PIM
* Search employee
* Search by employee ID
* Reset search
* Open Add Employee
* Add employee
* Employee validation

### Employee

* Search employee
* Invalid employee search
* Employee details

### Leave

* Open Leave
* Verify Leave List
* Open Apply Leave
* Open My Leave

### Recruitment

* Open Recruitment
* Search candidate
* Open Add Candidate
* Enter candidate information

### Admin

* Open Admin
* Search user
* Reset search
* Open Add User

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project:

```bash
cd OrangeHRMAutomation
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Install Chromium:

```bash
python -m playwright install chromium
```

## Configuration

Create `.env`:

```text
BASE_URL=https://opensource-demo.orangehrmlive.com/
USERNAME=Admin
PASSWORD=admin123
BROWSER=chromium
HEADLESS=false
SLOW_MO=0
```

## Run Tests

Run complete suite:

```bash
python -m pytest
```

Run smoke tests:

```bash
python -m pytest -m smoke
```

Run regression tests:

```bash
python -m pytest -m regression
```

Run login tests:

```bash
python -m pytest -m login
```

Run PIM tests:

```bash
python -m pytest -m pim
```

## Allure Report

Execute tests:

```bash
python -m pytest
```

Generate report:

```bash
allure generate allure-results -o allure-report --clean
```

Open report:

```bash
allure open allure-report
```

Or directly:

```bash
allure serve allure-results
```

## Reporting Features

The framework supports:

* Test execution status
* Test steps
* Test severity
* Test categories
* Failure screenshots
* Playwright trace attachments
* Test duration
* Test suites
* Smoke/regression grouping

## Framework Features

* Page Object Model
* Reusable Base Page
* Pytest fixtures
* Environment configuration
* Dynamic test data
* Allure reporting
* Failure screenshots
* Playwright tracing
* Logging
* Pytest markers
* Headless/headed execution
* Modular test organization

## Author

QA Automation Engineer

**Skills:** Python | Playwright | Pytest | POM | Selenium | API Testing | Git | GitHub | Allure
