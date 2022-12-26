from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication, QMainWindow
from controller import Controller
from model import Model
from view import View


class MainWindow(QMainWindow):
    """The main window for the app."""
    def __init__(self):
        super().__init__()

        self.setMinimumSize(QSize(450, 200))
        self.set_up_window()

    def set_up_window(self):
        m = Model()
        c = Controller()
        v = View(m, c)
        self.setCentralWidget(v)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
