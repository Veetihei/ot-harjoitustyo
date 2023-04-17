from tkinter import ttk, constants
from services.course_service import course_service


class LoginView:
    def __init__(self, root, handle_register, show_courses_view):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_register = handle_register
        self._show_courses_view = show_courses_view
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Tervetuloa! Kirjaudu sisään")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._handle_signin
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Rekisteröidy",
            command=self._handle_register
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        register_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def _handle_signin(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        course_service.login(username_value, password_value)
        self._show_courses_view()

        print(f"Käyttäjätunnus on: {username_value}")
        print(f"Salasana on: {password_value}")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
