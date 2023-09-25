from models.person import Person

class Student(Person):
    # Esta clase hereda de la clase Person y para esto debemos igualar los constructores
    def __init__(self, id: str, first_name: str, last_name: str) -> None:
        super().__init__(id, first_name, last_name)
        self.__registration_date = ''

    def get_registration_date(self) -> str:
        return self.__registration_date
    
    def set_registration_date(self, value: str) -> None:
        # Realizaremos algunas validaciones
        ERROR_MESSAGE = "ERROR: La fecha es incorrecta, el formato es dd/MM/yyyy."
        if len(value) != 10:
            print(ERROR_MESSAGE)
        elif "/" not in value: 
            print(ERROR_MESSAGE)
        elif int(value.split("/")[0]) < 1 or int(value.split("/")[0]) > 31:
            print(ERROR_MESSAGE)
        elif int(value.split("/")[1]) < 1 or int(value.split("/")[1]) > 12:
            print(ERROR_MESSAGE)
        elif len(value.split("/")[2]) != 4:
            print(ERROR_MESSAGE)
        else:
            self.__registration_date = value