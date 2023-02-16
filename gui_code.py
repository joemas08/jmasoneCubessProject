from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout,\
    QVBoxLayout, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit
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
        users = []
        while query.next():
            users.append(f'{query.value(first_name)} {query.value(last_name)}')

        page_layout = QHBoxLayout()
        button_layout = QVBoxLayout()
        submission_info_layout = QGridLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(submission_info_layout)

        submission_info_layout.addWidget(QLabel("Prefix: ", self), 0, 0)
        prefix_widget = QLineEdit()
        prefix_widget.setPlaceholderText("Mr.")
        prefix_widget.setReadOnly(True)
        submission_info_layout.addWidget(prefix_widget, 0, 1)
        submission_info_layout.addWidget(QLabel("First Name: ", self), 0, 3)
        first_name_widget = QLineEdit()
        first_name_widget.setPlaceholderText("John")
        first_name_widget.setReadOnly(True)
        submission_info_layout.addWidget(first_name_widget, 0, 4)
        submission_info_layout.addWidget(QLabel("Test Label5", self), 2, 0)

        for user in users:
            widget = QPushButton(f'{user}', self)
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