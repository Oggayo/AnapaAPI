import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QComboBox, QCheckBox, QPushButton, QLabel


class MainWindow(QWidget):
    def init(self):
        super().init()
        self.init_ui()

    def init_ui(self):
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("text?")

        self.combo_box = QComboBox()
        self.combo_box.addItem("where")
        self.combo_box.addItem("your")
        self.combo_box.addItem("mativation!")

        checkbox = QCheckBox('dont click me')
        checkbox.setChecked(False)
        checkbox.stateChanged.connect(self.checkbox_changed)

        button = QPushButton("pls dont click me...")
        button.clicked.connect(self.button_fun)

        dontclickable_label = QLabel("you cannot click me! I'am text label! Huh :3")

        vertical = QVBoxLayout()
        vertical.addWidget(checkbox)
        vertical.addWidget(button)
        vertical.addWidget(dontclickable_label)
        vertical.addWidget(self.line_edit)
        vertical.addWidget(self.combo_box)
        self.setLayout(vertical)

        self.setWindowTitle('test')

    def checkbox_changed(self, state):
        if state == 2:
            print('WHY U CLICK ME? (enabled)')
        else:
            print('YOU CLICK ME AGAIN! (disable)')

    def button_fun(self):
        print("sempay, i tell you, DONT CLICK ME!!!!!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "main":
    main()