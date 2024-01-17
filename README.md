<h1 align="center">CUBES Project</h1>
<br>
<h3>Joseph Masone</h3>
<br>
<h4>Brief overview of the project</h4>
<p>This project utilizes the API from <a href="https://www.wufoo.com">wufoo.com</a> that is used with their form 
submissions. It pulls all the submissions to a specified form and currently sends this information to a designated database 
in the project called form_submission.db. This database file will be created on the first run of the program. 
After the database is created a menu will appear with two buttons. One will update the wufoo data and the other 
will display a reactive <a href="https://pypi.org/project/PyQt5/">PyQt5</a> GUI with 
all of the submitters to <a href="https://j1masone.wufoo.com/forms/cubes-project-proposal-submission/">my wufoo form</a> 
and their correlating information when they are clicked on. A submitters project can be claimed by a user by clicking the
claim button and filling out their information. Once a project has been claimed their buttons color will indicate their 
status as well as showing what email has claimed them once the GUI window has been relaunched.</p>
<br>
<h4>Database Used</h4>
<p>I have used a SQLite database. It has the one table <i>form_submissions</i> that has all the correlating fields from my wufoo form.</p>
<br>
<h4>How to install & run the project</h4>
<ol>Clone the Repository</ol>
<ol>Run main.py on your machine</ol>
<br>
<h4>What was used to create the project</h4>
<ol>Pycharm 2022.3.1</ol>
<ol>Visual Studio Code</ol>
<ol>Python 3.10.0</ol>
