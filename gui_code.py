from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome GUI")
        users = ['user1', 'user2', 'user3', 'user4']

        label = QLabel("This is awesome!")

        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        page_layout = QVBoxLayout()
        button_layout = QVBoxLayout()

        page_layout.addLayout(button_layout)

        for user in users:
            button_layout.addWidget(QPushButton(f'{user}', self))

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)
