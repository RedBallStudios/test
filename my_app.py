from PyQt5.QtWidgets import QApplication
from instr import MainWin

app = QApplication([])

main_win = MainWin()
main_win.show()

app.exec_()
