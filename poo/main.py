class Person:
    def __init__(self, name: str, age: str) -> None:
        self.__name = name
        self.__age = age

    def set_name(self, value: str) -> None:
        if isinstance(value, str) and value:
            self.__name = value
        else:
            raise ValueError("El nombre debe ser una cadena no vacia")
    
    def get_name(self) -> str:
        return self.__name
    
    @property
    def age(self) -> int:
        return self.__age
    
    @age.setter
    def age(self, value: int) -> None:
        if isinstance(value, int) and value > 18:
            self.__age = value
        else:
            raise ValueError("La edad debe ser entera y mayor o igual que 18")
    

    
persona = Person("Pedro", 20)
persona.age = 30
print(persona.age)
