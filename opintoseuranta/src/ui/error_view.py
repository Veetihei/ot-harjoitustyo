from tkinter import ttk, constants
from services.course_service import course_service


class ErrorView:
    def __init__(self, root, error_message, previous_page):
        self._root = root
        self._error_message = error_message
        self._page = previous_page
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Jokin meni pieleen!", font=20)

        error_label = ttk.Label(master=self._frame, text=self._error_message)

        back_button = ttk.Button(
            master=self._frame,
            text="Palaa takaisin",
            command=self._page
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        error_label.grid(row=1, padx=5, pady=5)

        back_button.grid(padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
