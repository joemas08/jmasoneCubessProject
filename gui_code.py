from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout,\
    QVBoxLayout, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit,\
    QCheckBox
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Wufoo Forms")

        db_connection = QSqlDatabase.addDatabase("QSQLITE")
        db_connection.setDatabaseName("form_submission.db")
        db_connection.open()

        query = QSqlQuery()
        query.exec("SELECT first_name, last_name FROM form_submissions")
        first_name, last_name = range(2)
        submissions = []
        while query.next():
            submissions.append(f'{query.value(first_name)}'
                               f' {query.value(last_name)}')

        page_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        submission_info_layout = QGridLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(submission_info_layout)

        def show_entries_data(entry_passed):
            # name = entry_passed.split()
            # results = []
            # entry_id, prefix, first_name, last_name, title, org_name, email, org_site,
            # phone,course_project, guest_speaker, site_visit, job_shadow, internships, 
            # career_panel, networking_event, use_permission, date_created, created_by, 
            # date_updated, updated_by = range(21)
            # query = QSqlQuery()
            # query.exec(f"SELECT * FROM form_submissions WHERE first_name LIKE {name[0]}")
            # while query.next():
            #     results.append(f'{query.value(entry_id)}')
            
            # ROW 1
            submission_info_layout.addWidget(QLabel("Position: ", self), 0, 0)
            position_widget = QLineEdit()
            position_widget.setPlaceholderText("Supreme Leader")
            position_widget.setReadOnly(True)
            submission_info_layout.addWidget(position_widget, 0, 1)

            submission_info_layout.addWidget(QLabel("Prefix: ", self), 0, 2)
            prefix_widget = QLineEdit()
            prefix_widget.setPlaceholderText("Mr.")
            prefix_widget.setReadOnly(True)
            submission_info_layout.addWidget(prefix_widget, 0, 3)

            # ROW 2
            submission_info_layout.addWidget(QLabel("First Name: ", self), 1, 0)
            first_name_widget = QLineEdit()
            first_name_widget.setPlaceholderText("John")
            first_name_widget.setReadOnly(True)
            submission_info_layout.addWidget(first_name_widget, 1, 1)

            submission_info_layout.addWidget(QLabel("Last Name: ", self), 1, 2)
            last_name_widget = QLineEdit()
            last_name_widget.setPlaceholderText("Doe")
            last_name_widget.setReadOnly(True)
            submission_info_layout.addWidget(last_name_widget, 1, 3)

            # ROW 3
            submission_info_layout.addWidget(QLabel("Organization: ", self), 2, 0)
            org_widget = QLineEdit()
            org_widget.setPlaceholderText("Generic Name Co.")
            org_widget.setReadOnly(True)
            submission_info_layout.addWidget(org_widget, 2, 1)

            submission_info_layout.addWidget(QLabel("Email: ", self), 2, 2)
            email_widget = QLineEdit()
            email_widget.setPlaceholderText("sample@vanilla.com")
            email_widget.setReadOnly(True)
            submission_info_layout.addWidget(email_widget, 2, 3)

            # ROW 4
            submission_info_layout.addWidget(
                QLabel("Permission for Org Name: "), 3, 0
                )
            permission_widget = QLineEdit()
            permission_widget.setPlaceholderText("Yes")
            permission_widget.setReadOnly(True)
            submission_info_layout.addWidget(permission_widget, 3, 1)

            submission_info_layout.addWidget(QLabel("Phone Number: ", self), 3, 2)
            phone_widget = QLineEdit()
            phone_widget.setPlaceholderText("555-555-5555")
            phone_widget.setReadOnly(True)
            submission_info_layout.addWidget(phone_widget, 3, 3)

            # CHECK BOXES
            course_project_box = QCheckBox("Course Project")
            course_project_box.setDisabled(True)
            submission_info_layout.addWidget(course_project_box, 4, 0)

            guest_speaker_box = QCheckBox("Guest Speaker")
            guest_speaker_box.setChecked(True)
            guest_speaker_box.setDisabled(True)
            submission_info_layout.addWidget(guest_speaker_box, 5, 0)

            site_visit_box = QCheckBox("Site Visit")
            site_visit_box.setDisabled(True)
            submission_info_layout.addWidget(site_visit_box, 6, 0)

            job_shadow_box = QCheckBox("Job Shadow")
            job_shadow_box.setDisabled(True)
            submission_info_layout.addWidget(job_shadow_box, 7, 0)

            internship_box = QCheckBox("Internships")
            internship_box.setDisabled(True)
            submission_info_layout.addWidget(internship_box, 8, 0)

            career_panel_box = QCheckBox("Career Panel")
            career_panel_box.setDisabled(True)
            submission_info_layout.addWidget(career_panel_box, 9, 0)

            networking_event_box = QCheckBox("Networking Event")
            networking_event_box.setDisabled(True)
            submission_info_layout.addWidget(networking_event_box, 10, 0)

        for user in submissions:
            button = QPushButton(f'{user}', self)
            button.clicked.connect(lambda: show_entries_data(button.text()))
            widget = button
            button_layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)


def display_gui():
    # Only need one Qapplication instance per application
    app = QApplication(sys.argv)

    window = MainWindow()

    # Windows are hidden by default
    window.show()

    app.exec_()
