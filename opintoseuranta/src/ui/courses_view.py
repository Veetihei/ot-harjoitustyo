from tkinter import ttk, constants
from services.course_service import course_service


class CoursesView:
    def __init__(self, root, _handle_logout, _handle_add_course):
        self._root = root
        self._handle_logout = _handle_logout
        self._handle_add_course = _handle_add_course
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Täältä näet kurssit")
        
        logout_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu ulos",
            command=self._logout_handler
        )

        add_course_button = ttk.Button(
            master=self._frame,
            text="Lisää kurssi",
            command=self._handle_add_course
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)
        
        logout_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        
        add_course_button.grid(row=4, column=3, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        
        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        self._handle_logout()
