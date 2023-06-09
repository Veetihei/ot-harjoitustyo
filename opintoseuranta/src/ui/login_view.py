from tkinter import ttk, constants
from services.course_service import course_service


class LoginView:
    """Käyttäjän sisäänkirjautumisesta vastaava näkymä
    """

    def __init__(self, root, handle_register, handle_signin):
        """Luokan konstruktori

        Args:
            root: Tkinter-elementti, jonka sisään näkymä alustetaan
            handle_register: Kutsuttava arvo, kun käyttäjä haluaa rekisteröidä uuden käyttäjän
            handle_signin: Kutsuttava arvo, kun käyttäjä kirjautuu sisään
        """
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_register = handle_register
        self._handle_signin = handle_signin
        self._frame = None

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(
            master=self._frame, text="Tervetuloa! Kirjaudu sisään")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame, show="*")

        login_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu",
            command=self._signin_handler
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

    def _signin_handler(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        if course_service.login(username_value, password_value) is not None:
            self._handle_signin()

    def pack(self):
        """Näyttää näkymän
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Tuhoaa näkymän
        """
        self._frame.destroy()
