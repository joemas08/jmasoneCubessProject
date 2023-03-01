from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys
from gui_code import display_gui
from handle_request_functions import get_wufoo_data
from database_functions import connect_to_database, create_entry_table, \
    insert_wufoo_data_to_table, close_db


class SelectionWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(SelectionWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Selection Window")

        self.button_layout = QHBoxLayout()
        self.page_layout = QVBoxLayout()

        self.display_message = QLabel("Please make a selection")
        self.display_message.setAlignment(Qt.AlignCenter)
        self.page_layout.addWidget(self.display_message)

        self.update_button = QPushButton("Update Data", self)
        self.update_button.clicked.connect(update_data)
        self.show_data_button = QPushButton("Show Cubes Project", self)
        self.show_data_button.clicked.connect(display_gui)
        self.button_layout.addWidget(self.update_button)
        self.button_layout.addWidget(self.show_data_button)
        self.page_layout.addLayout(self.button_layout)

        # Adding page layout to widget to be displayed
        self.widget = QWidget()
        self.widget.setLayout(self.page_layout)
        self.setCentralWidget(self.widget)


def update_data():
    url = ("https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
           "submission/entries/json")

    form_entries = get_wufoo_data(url)

    database = 'form_submission.db'
    table_name = 'form_submissions'

    db_connection, db_cursor = connect_to_database(database)
    create_entry_table(db_connection, db_cursor, table_name)
    insert_wufoo_data_to_table(db_connection, db_cursor,
                               form_entries, table_name)
    close_db(db_connection, db_cursor)


def display_selection_gui():
    # Only need one Qapplication instance per application
    app = QApplication(sys.argv)

    window = SelectionWindow()

    # Windows are hidden by default
    window.show()

    app.exec_()
