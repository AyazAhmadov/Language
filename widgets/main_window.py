from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader

from constants import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setFixedSize(width, height)
        self.ui = self.load_ui()

        translate_icon_path = 'assets/translate.png'
        add_icon_path = 'assets/add.png'
        flashcard_icon_path = 'assets/flashcard.png'
        edit_icon_path = 'assets/edit.png'

        self.ui.side_menu_frame.setMinimumWidth(300)

        # Setting texts to buttons
        self.ui.toggle_button.setText('Toggle Menu')
        self.ui.go_to_add_button.setText('Add')
        self.ui.go_to_flashcards_button.setText('Flashcards')
        self.ui.go_to_translate_button.setText('Translate')
        self.ui.go_to_edit_button.setText('Edit')

        # Setting icons to buttons
        add_icon = QIcon(add_icon_path)
        self.ui.go_to_add_button.setIcon(add_icon)

        flashcards_icon = QIcon(flashcard_icon_path)
        self.ui.go_to_flashcards_button.setIcon(flashcards_icon)

        translate_icon = QIcon(translate_icon_path)
        self.ui.go_to_translate_button.setIcon(translate_icon)

        edit_icon = QIcon(edit_icon_path)
        self.ui.go_to_edit_button.setIcon(edit_icon)

        self.ui.toggle_button.clicked.connect(self.toggle_side_menu)

        self.toggle = False
        
        self.show()

    def load_ui(self):
        ui_file = QFile('ui/main_window.ui')
        loader =QUiLoader()
        ui_file.open(QFile.ReadOnly)
        ui = loader.load(ui_file, parentWidget=self)
        ui_file.close()

        return ui

    def toggle_side_menu(self):
        offset = 230
        side_menu_start_width = self.ui.side_menu_frame.width()

        if self.toggle:
            side_menu_end_width = side_menu_start_width + offset
        else:
            side_menu_end_width = side_menu_start_width - offset

        self.side_menu_animation = QPropertyAnimation(self.ui.side_menu_frame, b'minimumWidth')
        self.side_menu_animation.setDuration(350)
        self.side_menu_animation.setStartValue(side_menu_start_width)
        self.side_menu_animation.setEndValue(side_menu_end_width)
        self.side_menu_animation.setEasingCurve(QEasingCurve.InOutCubic)

        self.side_menu_animation.start()

        self.toggle = not self.toggle