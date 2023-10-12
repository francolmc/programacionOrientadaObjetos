class Client:
    def __init__(self, id: int) -> None:
        self.__id = id
        self.firs_name = ""
        self.last_name = ""
        self.__email = ""
        self.address = ""
        self.credit_card = ""

    def get_id(self) -> int:
        return self.__id

    def show(self):
        print(f"{self.firs_name} {self.last_name} {self.__email}")

    def get_email(self) -> str:
        return self.__email
    
    def set_email(self, value: str) -> None:
        # Antes de asignar el valor hacemos algunas validaciones
        ERROR_MESSAGE = "ERROR: El correo no es valido."
        if "@" not in value:
            if "." not in value:
                raise ValueError(ERROR_MESSAGE)
        else:
            self.__email = value