from tkinter import Tk, ttk, constants
from ui.login_view import LoginView
from ui.register_view import RegisterView
from ui.courses_view import CoursesView
from ui.add_course_view import AddCourseView
from ui.edit_course_view import EditCourseView
from ui.error_view import ErrorView


class UI:
    """Sovelluksen käyttöliittymästä vastaava luokka
    """

    def __init__(self, root):
        """Luokan konstruktori

        Args:
            root: Tkinter-elementti, jonka sisään käyttöliittymä alustetaan
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Käynnistää käyttöliittymän
        """
        self._show_login_view()

    def _hide_current_view(self):
        """Piilottaa nykyisen näkymän
        """
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _show_login_view(self):
        """Näyttää login näkymän
        """
        self._hide_current_view()
        self._root.geometry("400x200")
        self._current_view = LoginView(
            self._root,
            self._show_register_view,
            self._show_courses_view
        )

        self._current_view.pack()

    def _show_courses_view(self):
        """Näyttää kurssien yhteenvetonäkymän
        """
        self._hide_current_view()
        self._root.geometry("800x500")

        self._current_view = CoursesView(
            self._root,
            self._show_login_view,
            self._show_add_course_view,
            self._show_edit_course_view,
            self._reload_courses_view
        )

        self._current_view.pack()

    def _reload_courses_view(self):
        """Päivittää kurssien yhteenvetonäkymän
        """
        self._show_courses_view()

    def _show_edit_course_view(self, course):
        """Näyttää kurssin muokkausnäkymän

        Args:
            course: kurssi, jonka muokkausnäkymä näytetään
        """
        self._hide_current_view()
        self._root.geometry("800x300")

        self._current_view = EditCourseView(
            self._root,
            course,
            self._show_courses_view,
            self._show_error_view,
            self._show_courses_view
        )
        self._current_view.pack()

    def _show_register_view(self):
        """Näyttää rekisteröintinäkymän
        """
        self._hide_current_view()
        self._root.geometry("600x300")

        self._current_view = RegisterView(
            self._root,
            self._show_login_view,
            self._show_courses_view,
            self._show_error_view,
            self._show_register_view
        )

        self._current_view.pack()

    def _show_add_course_view(self):
        """Näyttää kurssinlisäytsnäkymän
        """
        self._hide_current_view()
        self._root.geometry("600x300")

        self._current_view = AddCourseView(
            self._root,
            self._show_courses_view,
            self._show_error_view,
            self._show_add_course_view
        )

        self._current_view.pack()

    def _show_error_view(self, message, previous_page):
        """Näyttää virhenäkymän

        Args:
            message: Näytettävä virheviesti
            previous_page: Edellinen sivu, johon voi palata
        """
        self._hide_current_view()
        self._root.geometry("600x300")
        self._current_view = ErrorView(
            self._root,
            message,
            previous_page
        )
        self._current_view.pack()
