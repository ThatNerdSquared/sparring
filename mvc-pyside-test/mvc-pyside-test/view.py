from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget  # noqa: E501
from model import TASKS


class View(QWidget):
    def __init__(self, m, c):
        super().__init__()

        self.CONTROLLER = c
        print(TASKS)
        layout = self.render()
        self.setLayout(layout)

    def render(self):
        layout = QVBoxLayout()
        for item in TASKS:
            lbl = QLabel(item)
            layout.addWidget(lbl)
        entrybox = QLineEdit()
        entryboop = QPushButton('Fire!')
        entryboop.clicked.connect(
            lambda: self.CONTROLLER.handle_add(
                entrybox.text(),
                self.onCallback
            )
        )
        layout.addWidget(entrybox)
        layout.addWidget(entryboop)
        return layout

    def onCallback(self):
        print(TASKS)
        layout = self.render()
        self.setLayout(layout)
        self.repaint()