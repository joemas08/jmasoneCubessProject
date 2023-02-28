from PyQt5.QtWidgets import QMainWindow, QApplication, \
    QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt
import sys


class IntroWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(IntroWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Selection Window")

        self.button_layout = QHBoxLayout()
        self.page_layout = QVBoxLayout()

        self.display_message = QLabel("Please make a selection")
        self.display_message.setAlignment(Qt.AlignCenter)
        self.page_layout.addWidget(self.display_message)

        self.button_1 = QPushButton("Update Data", self)
        self.button_2 = QPushButton("Show Cubes Project", self)
        self.button_layout.addWidget(self.button_1)
        self.button_layout.addWidget(self.button_2)
        self.page_layout.addLayout(self.button_layout)

        # Adding page layout to widget to be displayed
        self.widget = QWidget()
        self.widget.setLayout(self.page_layout)
        self.setCentralWidget(self.widget)


def display_selection_gui():
    # Only need one Qapplication instance per application
    app = QApplication(sys.argv)

    window = IntroWindow()

    # Windows are hidden by default
    window.show()

    app.exec_()
