from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.courses_view import CoursesView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()
        
        self._current_view = None

    def _handle_register(self):
        self._show_register_view()

    def _handle_signin(self):
        self._show_login_view()


    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginView(
            self._root,
            self._handle_register,
            self._show_courses_view
        )

        self._current_view.pack()

    def _show_courses_view(self):
        self._hide_current_view()

        self._current_view = CoursesView(
            self._root
        )

        self._current_view.pack()

    def _show_register_view(self):
        self._hide_current_view()

        self._current_view = RegisterView(
            self._root,
            self._handle_signin,
            self._show_courses_view
        )

        self._current_view.pack()


