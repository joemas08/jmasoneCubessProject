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
        submissions = []
        while query.next():
            submissions.append(f'{query.value("first_name")}'
                               f' {query.value("last_name")}')

        page_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        submission_info_layout = QGridLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(submission_info_layout)

        # ROW 1
        submission_info_layout.addWidget(QLabel("Position: ", self), 0, 0)
        position_widget = QLineEdit()
        position_widget.setReadOnly(True)
        submission_info_layout.addWidget(position_widget, 0, 1)

        submission_info_layout.addWidget(QLabel("Prefix: ", self), 0, 2)
        prefix_widget = QLineEdit()
        prefix_widget.setReadOnly(True)
        submission_info_layout.addWidget(prefix_widget, 0, 3)

        # ROW 2
        submission_info_layout.addWidget(QLabel("First Name: ", self), 1, 0)
        first_name_widget = QLineEdit()
        first_name_widget.setReadOnly(True)
        submission_info_layout.addWidget(first_name_widget, 1, 1)

        submission_info_layout.addWidget(QLabel("Last Name: ", self), 1, 2)
        last_name_widget = QLineEdit()
        last_name_widget.setReadOnly(True)
        submission_info_layout.addWidget(last_name_widget, 1, 3)

        # ROW 3
        submission_info_layout.addWidget(QLabel("Organization: ", self), 2, 0)
        org_widget = QLineEdit()
        org_widget.setReadOnly(True)
        submission_info_layout.addWidget(org_widget, 2, 1)

        submission_info_layout.addWidget(QLabel("Email: ", self), 2, 2)
        email_widget = QLineEdit()
        email_widget.setReadOnly(True)
        submission_info_layout.addWidget(email_widget, 2, 3)

        # ROW 4
        submission_info_layout.addWidget(
            QLabel("Permission for Org Name: "), 3, 0
            )
        permission_widget = QLineEdit()
        permission_widget.setReadOnly(True)
        submission_info_layout.addWidget(permission_widget, 3, 1)

        submission_info_layout.addWidget(QLabel("Phone Number: ", self), 3, 2)
        phone_widget = QLineEdit()
        phone_widget.setReadOnly(True)
        submission_info_layout.addWidget(phone_widget, 3, 3)

        # CHECK BOXES
        course_project_box = QCheckBox("Course Project")
        course_project_box.setDisabled(True)
        submission_info_layout.addWidget(course_project_box, 4, 0)

        guest_speaker_box = QCheckBox("Guest Speaker")
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

        def show_entries_data(entry_passed):
            name = entry_passed.split(' ')
            # name = ["James", "Bond"]

            entry_data = query_entries_data(name)
            print(entry_data)

            title, prefix, first, last, org_name, email, permission, phone, course, guest, site, job_shadow, internship, career_panel, networking = range(15)

            # ROW 1
            position_widget.setPlaceholderText(entry_data[title])
            prefix_widget.setPlaceholderText(entry_data[prefix])

            # ROW 2
            first_name_widget.setPlaceholderText(entry_data[first])
            last_name_widget.setPlaceholderText(entry_data[last])

            # ROW 3
            org_widget.setPlaceholderText(entry_data[org_name])
            email_widget.setPlaceholderText(entry_data[email])

            # ROW 4
            permission_widget.setPlaceholderText(entry_data[permission])
            phone_widget.setPlaceholderText(entry_data[phone])

            # CHECK BOXES
            if entry_data[course] != '':
                course_project_box.setChecked(True)
            else:
                course_project_box.setChecked(False)

            if entry_data[guest] != '':
                guest_speaker_box.setChecked(True)
            else:
                guest_speaker_box.setChecked(False)

            if entry_data[site] != '':
                site_visit_box.setChecked(True)
            else:
                site_visit_box.setChecked(False)

            if entry_data[job_shadow] != '':
                job_shadow_box.setChecked(True)
            else:
                job_shadow_box.setChecked(False)

            if entry_data[internship] != '':
                internship_box.setChecked(True)
            else:
                internship_box.setChecked(False)

            if entry_data[career_panel] != '':
                career_panel_box.setChecked(True)
            else:
                career_panel_box.setChecked(False)

            if entry_data[networking] != '':
                networking_event_box.setChecked(True)
            else:
                networking_event_box.setChecked(False)

        for user in submissions:
            button = QPushButton(f'{user}', self)
            button.clicked.connect(lambda: show_entries_data(button.text()))
            widget = button
            button_layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)


def query_entries_data(name_passed):

    entry_data = []

    query = QSqlQuery()
    query.exec(f"SELECT * FROM form_submissions WHERE first_name IN"
               f" (\"{name_passed[0]}\") AND last_name IN (\"{name_passed[1]}\")")
    while query.next():
        entry_data.append(query.value("title"))
        entry_data.append(query.value("prefix"))
        entry_data.append(query.value("first_name"))
        entry_data.append(query.value("last_name"))
        entry_data.append(query.value("org_name"))
        entry_data.append(query.value("email"))
        entry_data.append(query.value("use_permission"))
        entry_data.append(query.value("phone"))
        entry_data.append(query.value("course_project"))
        entry_data.append(query.value("guest_speaker"))
        entry_data.append(query.value("site_visit"))
        entry_data.append(query.value("job_shadow"))
        entry_data.append(query.value("internships"))
        entry_data.append(query.value("career_panel"))
        entry_data.append(query.value("networking_event"))

    return entry_data


def display_gui():
    # Only need one Qapplication instance per application
    app = QApplication(sys.argv)

    window = MainWindow()

    # Windows are hidden by default
    window.show()

    app.exec_()
