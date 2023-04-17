from tkinter import ttk, constants
from services.course_service import course_service


class EditCourseView:
    def __init__(self, root, course, handle_cancel):
        self._root = root
        self._user = course_service.get_current_user()
        self._course = course
        self._course_name_entry = None
        self._course_weight_entry = None
        self._course_grade_entry = None
        self._handle_cancel = handle_cancel
        self._frame = None

        self._initialize()

    def _initialize_course(self, course):

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

        course_name_label.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_weight_label.grid(
            row=3,
            column=3,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )
        course_grade_label.grid(
            row=3,
            column=6,
            columnspan=2,
            sticky=constants.W,
            padx=5,
            pady=5
        )

    def _initialize_courses_title(self):
        page_title = ttk.Label(
            master=self._frame, text="Muokkaa kurssia. Voit jättää kenttiä tyhjäksi.", font=18)

        course_name_title = ttk.Label(
            master=self._frame,
            text="Kurssin Nimi",
            font=10
        )
        course_weight_title = ttk.Label(
            master=self._frame,
            text="Kurssin opintopisteet",
            font=10
        )
        course_grade_title = ttk.Label(
            master=self._frame,
            text="Kurssin arvosana",
            font=10
        )

        page_title.grid(row=0, columnspan=5, padx=5, pady=5)

        course_name_title.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )
        course_weight_title.grid(
            row=1,
            column=3,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )
        course_grade_title.grid(
            row=1,
            column=6,
            columnspan=2,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5
        )

    def _initialize_edit_panel(self):

        course_name_label = ttk.Label(master=self._frame, text="Uusi Nimi:")
        self._course_name_entry = ttk.Entry(master=self._frame)

        course_weight_label = ttk.Label(
            master=self._frame, text="Uudet opintopisteet")
        self._course_weight_entry = ttk.Entry(master=self._frame)

        course_grade_label = ttk.Label(
            master=self._frame, text="Uusi arvosana")
        self._course_grade_entry = ttk.Entry(master=self._frame)

        course_name_label.grid(row=4, column=0, padx=5, pady=5)
        self._course_name_entry.grid(row=5, column=0, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        course_weight_label.grid(row=4, column=3, padx=5, pady=5)
        self._course_weight_entry.grid(row=5, column=3, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        course_grade_label.grid(row=4, column=6, padx=5, pady=5)
        self._course_grade_entry.grid(row=5, column=6, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_courses_title()
        self._initialize_course(self._course)
        self._initialize_edit_panel()

        add_course_button = ttk.Button(
            master=self._frame,
            text="Muokkaa",
            command=self._edit_course_handler
        )

        cancel_button = ttk.Button(
            master=self._frame,
            text="Peruuta",
            command=self._handle_cancel
        )

        add_course_button.grid(row=6, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        cancel_button.grid(row=6, column=2, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def _edit_course_handler(self):
        user_name = self._user.username

        course_name_value = self._course_name_entry.get()
        if len(course_name_value) == 0:
            course_name_value = self._course.name

        course_weight_value = self._course_weight_entry.get()
        if len(course_weight_value) == 0:
            course_weight_value = self._course.weight

        course_grade_value = self._course_grade_entry.get()
        if len(course_grade_value) == 0:
            course_grade_value = self._course.grade

        course_service.delete_course(self._course.id)
        course_service.add_new_course(
            user_name,
            course_name_value,
            course_weight_value,
            course_grade_value
        )
        self._handle_cancel()

        # try:
        #     course_service.add_new_course(
        #         user_name,
        #         course_name_value,
        #         course_weight_value,
        #         course_grade_value
        #     )
        #     self._handle_cancel()
        # except:
        #     print("Kurssin lisäys ei onnistunut")
        #     self._handle_cancel()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
