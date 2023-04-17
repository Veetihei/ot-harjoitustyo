from tkinter import ttk, constants
from services.course_service import course_service

class CoursesView:
    def __init__(self, root):
        self._root = root

        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Täältä näet kurssit")

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)


    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

