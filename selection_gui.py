from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
)
from PyQt5.QtCore import Qt
import sys
from gui_code import display_gui
from handle_request_functions import get_wufoo_data
from database_functions import (
    connect_to_database,
    create_entry_table,
    insert_wufoo_data_to_table,
    create_user_table,
    close_db,
)


class SelectionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selection Window")
        self.setFixedSize(400, 100)

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
        self.setLayout(self.page_layout)


def update_data():
    url = (
        "https://j1masone.wufoo.com/api/v3/forms/cubes-project-proposal-"
        "submission/entries/json"
    )

    form_entries = get_wufoo_data(url)

    database = "form_submission.db"
    submission_table_name = "form_submissions"

    db_connection, db_cursor = connect_to_database(database)
    create_user_table(db_connection, db_cursor)
    create_entry_table(db_connection, db_cursor, submission_table_name)
    insert_wufoo_data_to_table(
        db_connection, db_cursor, form_entries, submission_table_name
    )
    close_db(db_connection, db_cursor)


def display_selection_gui():
    app = QApplication(sys.argv)

    window = SelectionWindow()
    window.show()

    app.exec_()
