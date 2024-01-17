<div align="center">

   <h1>Capstone Project</h1>

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15.4-green.svg)](https://pypi.org/project/PyQt5/)
[![SQLite3](https://img.shields.io/badge/SQLite3-3.36.0-orange.svg)](https://www.sqlite.org/)
[![pytest](https://img.shields.io/badge/pytest-6.2.5-purple.svg)](https://pypi.org/project/pytest/)

</div>

![GUI Screenshot](/gui_screenshot.png)

## Project Overview

This project leverages the API provided by [wufoo.com](https://www.wufoo.com) to manage form submissions. The primary functionality involves retrieving submissions from a specified form on Wufoo and storing this information in a designated database file named `form_submission.db`. The database file is created on the initial run of the program.

## Features

1. **Data Retrieval:**

   - Pulls all submissions from the specified Wufoo form.

2. **Database Management:**

   - Creates and utilizes a SQLite database (`form_submission.db`) to store form submission data.

3. **User Interface:**

   - Displays a menu with two buttons after the database is created.
   - Updates Wufoo data: One button to refresh and update the data from Wufoo.
   - Reactive PyQt5 GUI: Another button to open a graphical user interface displaying all submitters to the [Wufoo form](https://j1masone.wufoo.com/forms/cubes-project-proposal-submission/).

4. **Submission Details:**

   - Clicking on a submitter's information in the GUI reveals detailed information about their submission.

5. **Project Claiming:**

   - Users can claim a submitter's project by clicking a claim button and providing their information.

6. **Status Indication:**

   - The GUI visually indicates the status of claimed projects through button color changes.

7. **Persistent Data:**
   - The claimed project's information, including the claiming user's email, is stored persistently and displayed upon relaunching the GUI.

## Getting Started

1. Ensure Python is installed on your system.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program.
   ```bash
   python main.py
   ```
4. Use the menu options to update Wufoo data or launch the PyQt5 GUI.

## Usage

- **Update Wufoo Data:**
- Click the corresponding button to fetch and update form submissions from Wufoo.

- **Launch GUI:**
- Click the button to open the PyQt5 GUI displaying submitter information.
- Click on a submitter's entry to view detailed information.
- Claim a project by clicking the claim button and providing necessary information.
