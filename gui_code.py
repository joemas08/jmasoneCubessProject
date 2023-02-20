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

        self.page_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()
        self.submission_info_layout = QGridLayout()

        self.page_layout.addLayout(self.button_layout)
        self.page_layout.addLayout(self.submission_info_layout)

        # ROW 1
        self.submission_info_layout.addWidget(QLabel("Position: ", self), 0, 0)
        self.position_widget = QLineEdit()
        self.position_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.position_widget, 0, 1)

        self.submission_info_layout.addWidget(QLabel("Prefix: ", self), 0, 2)
        self.prefix_widget = QLineEdit()
        self.prefix_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.prefix_widget, 0, 3)

        # ROW 2
        self.submission_info_layout.addWidget(QLabel("First Name: ", self), 1, 0)
        self.first_name_widget = QLineEdit()
        self.first_name_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.first_name_widget, 1, 1)

        self.submission_info_layout.addWidget(QLabel("Last Name: ", self), 1, 2)
        self.last_name_widget = QLineEdit()
        self.last_name_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.last_name_widget, 1, 3)

        # ROW 3
        self.submission_info_layout.addWidget(QLabel("Organization: ", self), 2, 0)
        self.org_widget = QLineEdit()
        self.org_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.org_widget, 2, 1)

        self.submission_info_layout.addWidget(QLabel("Email: ", self), 2, 2)
        self.email_widget = QLineEdit()
        self.email_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.email_widget, 2, 3)

        # ROW 4
        self.submission_info_layout.addWidget(
            QLabel("Permission for Org Name: "), 3, 0
            )
        self.permission_widget = QLineEdit()
        self.permission_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.permission_widget, 3, 1)

        self.submission_info_layout.addWidget(QLabel("Phone Number: ", self), 3, 2)
        self.phone_widget = QLineEdit()
        self.phone_widget.setReadOnly(True)
        self.submission_info_layout.addWidget(self.phone_widget, 3, 3)

        # CHECK BOXES
        self.course_project_box = QCheckBox("Course Project")
        self.course_project_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.course_project_box, 4, 0)

        self.guest_speaker_box = QCheckBox("Guest Speaker")
        self.guest_speaker_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.guest_speaker_box, 5, 0)

        self.site_visit_box = QCheckBox("Site Visit")
        self.site_visit_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.site_visit_box, 6, 0)

        self.job_shadow_box = QCheckBox("Job Shadow")
        self.job_shadow_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.job_shadow_box, 7, 0)

        self.internship_box = QCheckBox("Internships")
        self.internship_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.internship_box, 8, 0)

        self.career_panel_box = QCheckBox("Career Panel")
        self.career_panel_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.career_panel_box, 9, 0)

        self.networking_event_box = QCheckBox("Networking Event")
        self.networking_event_box.setDisabled(True)
        self.submission_info_layout.addWidget(self.networking_event_box, 10, 0)

        def show_entries_data():
            name = self.sender().text()
            name = name.split()

            entry_data = query_entries_data(name)

            title, prefix, first, last, org_name, email, permission, phone, course, guest, site, job_shadow, internship, career_panel, networking = range(15)

            # ROW 1
            self.position_widget.setPlaceholderText(entry_data[title])
            self.prefix_widget.setPlaceholderText(entry_data[prefix])

            # ROW 2
            self.first_name_widget.setPlaceholderText(entry_data[first])
            self.last_name_widget.setPlaceholderText(entry_data[last])

            # ROW 3
            self.org_widget.setPlaceholderText(entry_data[org_name])
            self.email_widget.setPlaceholderText(entry_data[email])

            # ROW 4
            self.permission_widget.setPlaceholderText(entry_data[permission])
            self.phone_widget.setPlaceholderText(entry_data[phone])

            # CHECK BOXES
            if entry_data[course] != '':
                self.course_project_box.setChecked(True)
            else:
                self.course_project_box.setChecked(False)

            if entry_data[guest] != '':
                self.guest_speaker_box.setChecked(True)
            else:
                self.guest_speaker_box.setChecked(False)

            if entry_data[site] != '':
                self.site_visit_box.setChecked(True)
            else:
                self.site_visit_box.setChecked(False)

            if entry_data[job_shadow] != '':
                self.job_shadow_box.setChecked(True)
            else:
                self.job_shadow_box.setChecked(False)

            if entry_data[internship] != '':
                self.internship_box.setChecked(True)
            else:
                self.internship_box.setChecked(False)

            if entry_data[career_panel] != '':
                self.career_panel_box.setChecked(True)
            else:
                self.career_panel_box.setChecked(False)

            if entry_data[networking] != '':
                self.networking_event_box.setChecked(True)
            else:
                self.networking_event_box.setChecked(False)

        for user in submissions:
            self.button = QPushButton(f'{user}', self)
            self.button.clicked.connect(lambda: show_entries_data())
            self.button_layout.addWidget(self.button)

        self.widget = QWidget()
        self.widget.setLayout(self.page_layout)
        self.setCentralWidget(self.widget)


def query_entries_data(name_passed):

    entry_data = []

    query = QSqlQuery()
    if len(name_passed) == 2:
        query.exec(f"SELECT * FROM form_submissions WHERE first_name IN"
                   f" (\"{name_passed[0]}\") AND last_name IN (\"{name_passed[1]}\")")
    else:
        query.exec(f"SELECT * FROM form_submissions WHERE first_name IN"
                   f" (\"{name_passed[0]}\") AND last_name IN (\"{name_passed[1]} {name_passed[2]}\")")
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
