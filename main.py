from PySide6.QtWidgets import QApplication
from widgets.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication()
    window = MainWindow()
    app.exec()