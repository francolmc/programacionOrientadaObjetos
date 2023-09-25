from models.person import Person

class Teacher(Person):
    def __init__(self, id: str, first_name: str, last_name: str) -> None:
        super().__init__(id, first_name, last_name)
        self.is_administrative = False