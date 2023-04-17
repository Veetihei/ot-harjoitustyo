from tkinter import ttk, constants
from services.course_service import course_service


class CoursesView:
    def __init__(self, root, _handle_logout, _handle_add_course):
        self._root = root
        self._user = course_service.get_current_user()
        self._handle_logout = _handle_logout
        self._handle_add_course = _handle_add_course
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Täältä näet kurssit")

        courses = course_service.get_courses_by_username(self._user.username)
        # print("Sisällä:", course_service.get_current_user())
        print(courses)

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

        course_name_title = ttk.Label(
            master=self._frame, text="Kurssin Nimi", font=15)
        course_name_title.grid(row=5, column=0, columnspan=3,
                               sticky=constants.W, padx=5, pady=5)

        course_weight_title = ttk.Label(
            master=self._frame, text="Kurssin opintopisteet", font=15)
        course_weight_title.grid(
            row=5, column=3, columnspan=3, sticky=constants.W, padx=5, pady=5)

        course_grade_title = ttk.Label(
            master=self._frame, text="Kurssin arvosana", font=15)
        course_grade_title.grid(
            row=5, column=6, columnspan=3, sticky=constants.W, padx=5, pady=5)

        row = 5
        for course in courses:
            row += 1
            course_name_label = ttk.Label(
                master=self._frame, text=course.name
            )
            course_name_label.grid(row=row, column=0, columnspan=3,
                                   sticky=constants.W, padx=5, pady=5)

            course_weight_label = ttk.Label(
                master=self._frame, text=course.weight
            )
            course_weight_label.grid(row=row, column=3, columnspan=3,
                                     sticky=constants.W, padx=5, pady=5)

            course_grade_label = ttk.Label(
                master=self._frame, text=course.grade
            )
            course_grade_label.grid(row=row, column=6, columnspan=3,
                                    sticky=constants.W, padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        self._handle_logout()
