from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from final_win import FinalWin

class TestWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Тест")
        self.resize(400, 300)

        self.question = QLabel("Сколько будет 2 + 2?")
        self.answer = QLineEdit()
        self.button = QPushButton("Ответить")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.question)
        self.layout.addWidget(self.answer)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.button.clicked.connect(self.check_answer)

    def check_answer(self):
        if self.answer.text() == "4":
            self.result = "Правильно!"
        else:
            self.result = "Неправильно!"

        self.fw = FinalWin(self.result)
        self.fw.show()
        self.hide()
