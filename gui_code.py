from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
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
        submission_info_layout = QVBoxLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(submission_info_layout)

        submission_info_layout.addWidget(QLabel("Test Label", self))

        for user in users:
            widget = QPushButton(f'{user}', self)
            button_layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)
