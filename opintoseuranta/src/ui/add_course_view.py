from tkinter import ttk, constants
from services.course_service import course_service


class AddCourseView:
    def __init__(self, root, handle_cancel):
        self._root = root
        self._course_name_entry = None
        self._course_weight_entry = None
        self._course_grade_entry = None
        self._handle_cancel = handle_cancel
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Lisää kurssi:")

        course_name_label = ttk.Label(master=self._frame, text="Kurssin Nimi:")
        self._course_name_entry = ttk.Entry(master=self._frame)

        course_weight_label = ttk.Label(master=self._frame, text="Kurssin opintopisteet")
        self._course_weight_entry = ttk.Entry(master=self._frame)

        course_grade_label = ttk.Label(master=self._frame, text="Kurssin arvosana")
        self._course_grade_entry = ttk.Entry(master=self._frame)

        add_course_button = ttk.Button(
            master=self._frame,
            text="Lisää",
            command=self._add_course_handler
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_cancel
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        course_name_label.grid(row=1, column=0, padx=5, pady=5)
        self._course_name_entry.grid(row=2, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        course_weight_label.grid(row=1, column=3, padx=5, pady=5)
        self._course_weight_entry.grid(row=2, column=3, sticky=(
            constants.E, constants.W), padx=5, pady=5)
        
        course_grade_label.grid(row=1, column=6, padx=5, pady=5)
        self._course_grade_entry.grid(row=2, column=6, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        add_course_button.grid(row=3, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        cancel_button.grid(row=4, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def _add_course_handler(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        if len(username_value) < 2 or len(password_value) < 2:
            return

        course_service.register(username_value, password_value)
        self._handle_register()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
