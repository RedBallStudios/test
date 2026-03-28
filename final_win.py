from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class FinalWin(QWidget):
    def __init__(self, result):
        super().__init__()

        self.setWindowTitle("Результат")
        self.resize(400, 300)

        self.label = QLabel("Результат теста:")
        self.result_label = QLabel(result)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)
