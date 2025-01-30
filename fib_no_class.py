#!/usr/bin/env python3
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
layout = QFormLayout(window)
n_input = QSpinBox()
n_input.setValue(1)
run_button = QPushButton("Run")
f_output = QLabel("")
layout.insertRow(0, QLabel("n = "), n_input)
layout.insertRow(1, run_button)
layout.insertRow(2, f_output)

def run_fib():
    n = n_input.value()
    fib = [0,1]
    while len(fib) <= n:
        fib.append(fib[-1] + fib[-2])
    f_output.setText(f"f({n}) = {fib[n]}")

run_button.clicked.connect(run_fib)

window.show()
app.exec()