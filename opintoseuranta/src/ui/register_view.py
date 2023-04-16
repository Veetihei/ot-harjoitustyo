from tkinter import ttk, constants

class RegisterView:
    def __init__(self, root, handle_signin):
        self._root = root
        self._username_entry = None
        self._password_entry = None
        self._handle_signin = handle_signin
        self._frame = None

        self._initialize()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        heading_label = ttk.Label(master=self._frame, text="Tee käyttäjätunnus:")

        username_label = ttk.Label(master=self._frame, text="Käyttäjätunnus")
        self._username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Salasana")
        self._password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(
            master=self._frame, 
            text="Rekisteröidy",
            command=self._handle_register
        )

        register_button = ttk.Button(
            master=self._frame,
            text="Kirjaudu sisään",
            command=self._handle_signin
        )

        heading_label.grid(row=0, column=0, columnspan=2, sticky=constants.W, padx=5, pady=5)

        username_label.grid(row=1, column=0, padx=5, pady=5)
        self._username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        password_label.grid(row=2, column=0, padx=5, pady=5)
        self._password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)

        login_button.grid(row=3, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        register_button.grid(row=4, column=0, columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)

        self._root.grid_columnconfigure(1, weight=10, minsize=300)

    def _handle_register(self):
        username_value = self._username_entry.get()
        password_value = self._password_entry.get()

        print(f"Uusi käyttäjätunnus on: {username_value}")
        print(f"Uusi salasana on: {password_value}")

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
