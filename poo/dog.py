class Animal:
    # Inicializador
    def __init__(self, name: str, sound: str) -> None:
        self.name = name
        self.sound = sound

    def make_sound(self) -> None:
        print(f"{self.name} hace {self.sound}")


class Dog(Animal):
    def __init__(self, name: str, sound: str) -> None:
        super().__init__(name, sound)

    def move_tail(self) -> None:
        print(f"{self.name} mueve la cola.")


perrito = Dog("Killer", "Guau!!!")
print(perrito.name)
print(perrito.sound)
perrito.make_sound()
perrito.move_tail()
