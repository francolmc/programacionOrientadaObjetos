class Persona: 
    # constante
    PI_VALUE = 3.14
    # atributo
    first_name_atribute = ""
    # encapsulamiento
    __age = 0

    # constructor o inicializador
    def __init__(self, first_name: str) -> None:
        self.first_name_atribute = first_name

    # metodos para manipular atributos privados
    def setAge(self, value: int) -> None:
        if value < 18:
            print("Error: la edad no puede ser menor que 18.")
        else:
            self.__age = value
    
    def getAge(self) -> int:
        return self.__age
    