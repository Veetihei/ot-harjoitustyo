from tkinter import ttk, constants
from services.course_service import course_service


class AddCourseView:
    """Kurssin lisäämisestä vastaava näkymä
    """

    def __init__(self, root, handle_cancel, handle_error, memory):
        """Luokan konstruktori

        Args:
            root: Tkinter elementti, jonka sisään näkymä alustetaan
            handle_cancel: Kutsuttava arvo, jota kutsutaan, kun halutaan palata takaisin
            handle_error: Kutsuttava arvo, jota kutsutaan kun halutaan näyttää virhe-viesti
            memory: Sivu jolle palataan virhenäkymästä
        """
        self._root = root
        self._user = course_service.get_current_user()
        self._course_name_entry = None
        self._course_weight_entry = None
        self._course_grade_entry = None
        self._handle_cancel = handle_cancel
        self._handle_error = handle_error
        self._memory = memory
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Lisää kurssi:")

        course_name_label = ttk.Label(master=self._frame, text="Kurssin Nimi:")
        self._course_name_entry = ttk.Entry(master=self._frame)

        course_weight_label = ttk.Label(
            master=self._frame, text="Kurssin opintopisteet")
        self._course_weight_entry = ttk.Entry(master=self._frame)

        course_grade_label = ttk.Label(
            master=self._frame, text="Kurssin arvosana")
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
        user_name = self._user.username
        course_name_value = self._course_name_entry.get()
        course_weight_value = self._course_weight_entry.get()
        course_grade_value = self._course_grade_entry.get()

        result = course_service.add_new_course(
            user_name,
            course_name_value,
            course_weight_value,
            course_grade_value
        )
        if result == True:
            self._handle_cancel()
        else:
            self._handle_error(result, self._memory)

    def pack(self):
        """Näyttää näkymän
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän
        """
        self._frame.destroy()
