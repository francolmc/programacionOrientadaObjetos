from models.student import Student
from models.teacher import Teacher

class Course():
    def __init__(self, id: str) -> None:
        self.__id = id
        self.__teacher = None
        self.__students = list()

    def get_id(self) -> int:
        return self.__id
    
    def get_teacher(self) -> Teacher:
        return self.__teacher

    def set_teacher(self, value: Teacher) -> None:
        ERROR_MESSAGE = "ERROR: El valor debe corresponder a un Profesor."
        if not isinstance(value, Teacher):
            raise ValueError(ERROR_MESSAGE)
        self.__teacher = value

    def get_students(self) -> list:
        return self.__students
    
    def add_student(self, value: Student) -> None:
        if not isinstance(value, Student):
            raise ValueError("ERROR: El valor debe corresponder a un Estudiante.")
        if self.searc_student_by_email(value.get_email()) != None:
            raise ValueError("ERROR: Ya existe un alumno registrado con este correo electronico.")
        self.__students.append(value)

    def searc_student_by_email(self, email: str) -> Student | None:
        item: Student
        for item in self.__students:
            if item.get_email() == email:
                return item
        return None
    
    def get_index_student(self, id: str) -> int:
        item: Student
        index = 0
        for item in self.__students:
            if item.get_id() == id:
                return index
            index = index + 1
        return -1
    
    def remove_student(self, id: int):
        index = self.get_index_student(id)
        if index >= 0:
            self.__students.pop(index)
