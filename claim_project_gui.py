from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QWidget,
    QLineEdit,
    QMainWindow,
)
from database_functions import claim_project

# I had an issue getting this window to display when the claim button was
# clicked. It would close immediatly after opening. I reworked the code so
# the window can be displayed in main if it's uncommented so you can see
# the window and what I was trying to do.


class ClaimWindow(QMainWindow):
    def __init__(self, parent, parent_first_name, parent_last_name):
        super().__init__(parent)

        self.setWindowTitle("Claim Project Window")
        self.setFixedSize(270, 225)

        self.parent_first_name = parent_first_name.placeholderText()
        self.parent_last_name = parent_last_name.placeholderText()

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.page_layout = QVBoxLayout(centralWidget)

        self.first_name_widget = QLineEdit()
        self.first_name_widget.setPlaceholderText("First Name")
        self.page_layout.addWidget(self.first_name_widget)

        self.last_name_widget = QLineEdit()
        self.last_name_widget.setPlaceholderText("Last Name")
        self.page_layout.addWidget(self.last_name_widget)

        self.title_widget = QLineEdit()
        self.title_widget.setPlaceholderText("Title")
        self.page_layout.addWidget(self.title_widget)

        self.email_widget = QLineEdit()
        self.email_widget.setPlaceholderText("BSU Email")
        self.page_layout.addWidget(self.email_widget)

        self.department_widget = QLineEdit()
        self.department_widget.setPlaceholderText("Department")
        self.page_layout.addWidget(self.department_widget)

        self.button = QPushButton("Claim", self)
        self.button.clicked.connect(self.send_claim)
        self.page_layout.addWidget(self.button)

        self.setLayout(self.page_layout)

    def send_claim(self):
        claim_project(
            self.first_name_widget.text(),
            self.last_name_widget.text(),
            self.title_widget.text(),
            self.email_widget.text(),
            self.department_widget.text(),
            self.parent_first_name,
            self.parent_last_name,
        )
        self.close()
