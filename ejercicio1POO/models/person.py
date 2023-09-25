class Person():
    def __init__(self, id: str, first_name: str, last_name: str) -> None:
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.__email = ""

    def get_id(self) -> str:
        return self.__id
    
    # Metodo para obtener el valor del correo electronico
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
        