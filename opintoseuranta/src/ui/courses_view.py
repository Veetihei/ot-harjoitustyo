from tkinter import ttk, constants
from services.course_service import course_service


class CoursesView:
    """Kurssien yleisnäkymästä vastaava näkymä
    """

    def __init__(self, root, handle_logout, handle_add_course, handle_edit_course, handle_reload):
        """Luokan konstruktori

        Args:
            root (_type_): Tkinter elementti, jonka sisään näkymä alustetaan
            handle_logout (_type_): Kutsuttava arvo, jota kutsutaan kun käyttäjä haluaa kirjautua ulos
            handle_add_course (_type_): Kutsuttava arvo, jota kutsutaan kun käyttäjä haluaa lisätä kurssin
            handle_edit_course (_type_): Kutsuttava arvo, jota kutsutaan kun käyttäjä haluaa muokata kurssia
            handle_reload (_type_): Kutsuttava-arvo, jota kutsutaan kun kurssinäkymä halutaan päivittää
        """
        self._root = root
        self._user = course_service.get_current_user()
        self._handle_logout = handle_logout
        self._handle_add_course = handle_add_course
        self._handle_edit_course = handle_edit_course
        self._handle_reload = handle_reload
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _logout_handler(self):
        self._handle_logout()

    def _course_stat_box(self, title, info, column):
        course_stat = ttk.LabelFrame(master=self._frame, text=title)
        stat_info = ttk.Label(master=course_stat, text=info)
        course_stat.grid(row=2, column=column, padx=5, pady=5)
        stat_info.grid(padx=5, pady=5)

    def _course_stat_handler(self):
        mean_grade, weight_sum, course_num = course_service.get_course_stats(
            self._user.username)
        self._course_stat_box("Keskiarvo", "{:.2f}".format(mean_grade), 0)
        self._course_stat_box("Opintopisteet", weight_sum, 2)
        self._course_stat_box("Suoritukset", course_num, 4)

    def _course_edit_handler(self, course):
        # course_service.edit_course(course, self._user.username)
        self._handle_edit_course(course)

    def _course_delete_handler(self, course_id):
        # print(course_id)
        course_service.delete_course(course_id)
        self._handle_reload()

    def _initialize_courses_title(self, row):
        course_name_title = ttk.Label(
            master=self._frame,
            text="Kurssin Nimi",
            font=15
        )

        course_weight_title = ttk.Label(
            master=self._frame,
            text="Kurssin opintopisteet",
            font=15
        )
        course_grade_title = ttk.Label(
            master=self._frame,
            text="Kurssin arvosana",
            font=15
        )

        course_name_title.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_weight_title.grid(
            row=row,
            column=3,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_grade_title.grid(
            row=row,
            column=6,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )

    def _initialize_course(self, row, course):

        course_name_label = ttk.Label(
            master=self._frame,
            text=course.name
        )
        course_weight_label = ttk.Label(
            master=self._frame,
            text=course.weight
        )
        course_grade_label = ttk.Label(
            master=self._frame,
            text=course.grade
        )
        course_edit_button = ttk.Button(
            master=self._frame,
            text="Muokkaa",
            command=lambda: self._course_edit_handler(course)
        )
        course_delete_button = ttk.Button(
            master=self._frame,
            text="Poista",
            command=lambda: self._course_delete_handler(course.id)
        )

        course_name_label.grid(
            row=row,
            column=0,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_weight_label.grid(
            row=row,
            column=3,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_grade_label.grid(
            row=row,
            column=6,
            columnspan=3,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_edit_button.grid(
            row=row,
            column=9,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_delete_button.grid(
            row=row,
            column=11,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )

    def _initialize_courses(self, row):
        courses = course_service.get_courses_by_username(self._user.username)

        self._initialize_courses_title(row)

        for course in courses:
            row += 1
            self._initialize_course(row, course)

    def _initialize_header(self):

        heading_label = ttk.Label(
            master=self._frame,
            text=f"Tervetuloa {self._user.username}!"
        )

        self._course_stat_handler()

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

        heading_label.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )

        logout_button.grid(
            row=7,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

        add_course_button.grid(
            row=7,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()

        row = 8
        self._initialize_courses(row)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)
