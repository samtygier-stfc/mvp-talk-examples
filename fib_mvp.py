#!/usr/bin/env python3
from __future__ import annotations

from PyQt5.QtWidgets import *


class FibWindowView(QWidget):
    presenter: FibWindowPresenter
    def __init__(self):
        super().__init__()
        layout = QFormLayout(self)
        self.n_input = QSpinBox()
        self.n_input.setValue(1)
        self.f_output = QLabel("")
        layout.insertRow(0, QLabel("n = "), self.n_input)
        self.run_button = QPushButton("Run")
        layout.insertRow(1, self.run_button)
        layout.insertRow(2, self.f_output)

        self.run_button.clicked.connect(self._handle_run_button)

    def set_presenter(self, presenter: FibWindowPresenter):
        self.presenter = presenter

    def _handle_run_button(self):
        self.presenter.run_calculation()

    def get_n(self) -> int:
        return self.n_input.value()

    def set_output(self, result: str):
        self.f_output.setText(result)

class FibWindowPresenter:
    def __init__(self, view: FibWindowView, model: FibModel):
        self.view = view
        self.model = model
        self.view.set_presenter(self)

    def run_calculation(self):
        n = self.view.get_n()
        f = self.model.run_fib(n)
        result = f"f({n}) = {f}"
        self.view.set_output(result)


class FibModel:
    def run_fib(self, n: int) -> int:
        fib = [0,1]
        while len(fib) <= n:
            fib.append(fib[-1] + fib[-2])
        return fib[n]


if __name__ == '__main__':
    app = QApplication([])

    view = FibWindowView()
    model = FibModel()
    presenter = FibWindowPresenter(view, model)

    view.show()
    app.exec()