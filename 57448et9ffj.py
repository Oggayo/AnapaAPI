import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import pyautogui

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
  
        self.label = QLabel(self)
        self.label.setText("Наведите и кликните мышью")
        self.label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("ЛКМ нажата")
        elif event.button() == Qt.RightButton:
            self.label.setText("ПКМ нажата")

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.label.setText("Двойной клик ЛКМ")
 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Обработка событий мыши")
    window.setGeometry(100, 100, 400, 200)
    window.show()
    sys.exit(app.exec_())
