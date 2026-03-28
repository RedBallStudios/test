from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout
from second_win import TestWin

class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Инструкция")
        self.resize(400, 300)

        self.title = QLabel("Тест на внимание")
        self.instruction = QLabel(
            "Нажмите кнопку, чтобы начать.\n"
            "Вам нужно будет пройти небольшой тест."
        )
        self.button = QPushButton("Начать")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.instruction)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = TestWin()
        self.tw.show()
        self.hide()
