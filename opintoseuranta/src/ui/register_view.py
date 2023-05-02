from tkinter import ttk, constants
from services.course_service import course_service


class RegisterView:
    """Käyttäjän rekisteröitymisestä vastaava näkymä
    """
    def __init__(self, root, handle_signin, handle_register, handle_error, memory):
        """Luokan konstruktori

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_signin (_type_): Kutsuttava arvo, kun käyttäjä haluaa kirjautua sisään
            handle_register (_type_): Kutsuttava arvo, kun käyttäjä haluaa rekisteröityä
            handle_error (_type_): Kutsuttava arvo, kun näytetään virheilmoitus
            memory (_type_): Näkymä, johon palataan virhesivulta
        """
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_signin = handle_signin
        self._handle_register = handle_register
        self._handle_error = handle_error
        self._memory = memory
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Tee käyttäjätunnus:", font=20)

        username_instruction_label = ttk.Label(
            master=self._frame, text="Käyttäjätunnuksessa ja salasanassa on oltava 3-10 merkkiä")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        check_password_label = ttk.Label(
            master=self._frame, text="Salasana uudestaan")
        self._check_password_entry = ttk.Entry(master=self._frame)

        register_button = ttk.Button(
            master=self._frame,
            text="Tee tunnus",
            command=self._register_handler
        )

        existing_user_label = ttk.Label(
            master=self._frame, text="Onko sinulla jo käyttäjätunnus?")

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_signin
        )

        heading_label.grid(row=0, column=0, columnspan=2,
                           sticky=constants.W, padx=5, pady=5)

        username_instruction_label.grid(row=1, padx=5, pady=5)

        username_label.grid(row=2, column=0, padx=5, pady=5)
        self._username_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=3, column=0, padx=5, pady=5)
        self._password_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        check_password_label.grid(row=4, padx=5, pady=5)
        self._check_password_entry.grid(row=4, column=1, padx=5, pady=5)

        register_button.grid(row=5, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        existing_user_label.grid(row=6, padx=5, pady=5)

        login_button.grid(row=7, column=0, columnspan=2, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def _register_handler(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()
        password_check = self._check_password_entry.get()

        result = course_service.register(
            username_value, password_value, password_check)
        if result == True:
            self._handle_register()
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
