from PyQt5.QtWidgets import QVBoxLayout, QPushButton, \
    QWidget, QLineEdit


class ClaimingWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Claim Project Window")

        self.page_layout = QVBoxLayout()

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
        self.page_layout.addWidget(self.button)

        self.setLayout(self.page_layout)


def display_claiming_gui():
    window = ClaimingWindow()

    window.show()
