#!/usr/bin/env python3
from __future__ import annotations
import unittest

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from PyQt5.QtTest import QTest

from fib_mvp_pure import FibModel, FibWindowView, FibWindowPresenter

from PyQt5.QtWidgets import *

app = QApplication([])

class FibSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.view = FibWindowView()
        self.model = FibModel()
        self.presenter = FibWindowPresenter(self.view, self.model)

        self.view.show()
        QTest.qWait(10)

    def tearDown(self):
        QTest.qWait(10)
        self.view.close()

    def test_calc_fib(self):
        QTest.mouseClick(self.view.run_button, Qt.LeftButton)
        self.assertEqual("f(1) = 1", self.view.f_output.text())

    def test_calc_fib_changed(self):
        QTest.keySequence(self.view.n_input, QKeySequence.SelectAll)
        QTest.keyClicks(self.view.n_input, "10")
        QTest.mouseClick(self.view.run_button, Qt.LeftButton)
        self.assertEqual("f(10) = 55", self.view.f_output.text())

class FibScreenShotTest(unittest.TestCase):
    def setUp(self) -> None:
        self.view = FibWindowView()
        self.model = FibModel()
        self.presenter = FibWindowPresenter(self.view, self.model)

        self.view.show()
        QTest.qWait(10)

    def tearDown(self):
        QTest.qWait(10)
        self.view.close()

    def _take_screen_shot(self, widget:QWidget, filename: str):
        QTest.qWaitForWindowExposed(widget)
        QApplication.sendPostedEvents()
        QApplication.processEvents()
        window_image = widget.grab()
        window_image.save(filename, "PNG")

    def test_calc_fib_new_window(self):
        self._take_screen_shot(self.view, "fib.png")

    def test_calc_fib_changed(self):
        QTest.keySequence(self.view.n_input, QKeySequence.SelectAll)
        QTest.keyClicks(self.view.n_input, "10")
        QTest.mouseClick(self.view.run_button, Qt.LeftButton)
        self._take_screen_shot(self.view, "fib_n10.png")