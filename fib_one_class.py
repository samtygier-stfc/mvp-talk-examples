#!/usr/bin/env python3
from PyQt5.QtWidgets import *


class FibWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)
        self.n_input = QSpinBox()
        self.n_input.setValue(1)
        run_button = QPushButton("Run")
        self.f_output = QLabel("")
        layout.insertRow(0, QLabel("n = "), self.n_input)
        layout.insertRow(1, run_button)
        layout.insertRow(2, self.f_output)

        run_button.clicked.connect(self.run_fib)

    def run_fib(self):
        n = self.n_input.value()
        fib = [0,1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        self.f_output.setText(f"f({n}) = {fib[n]}")

if __name__ == '__main__':
    app = QApplication([])
    window = FibWindow()
    window.show()
    app.exec()