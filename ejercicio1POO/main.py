from models.course import Course
from models.student import Student
from models.teacher import Teacher

# Crear la instancia u objecto que repsente al curso
poo_course = Course("POO_001")
# Ingresar un profesor y asignarlo al curso
def add_teacher():
    try:
        print("Registrar profesor")
        poo_teacher_first_name = input("Ingrese el nombre del profesor: ")
        poo_teacher_last_name = input("Ingrese el apellido del profesor: ")
        poo_teacher = Teacher("TEACH_001", poo_teacher_first_name, poo_teacher_last_name)
        poo_teacher_email = input("Ingrese el email del profesor: ")
        poo_teacher.set_email(poo_teacher_email)
        global poo_course
        poo_course.set_teacher(poo_teacher)
    except ValueError as e:
        print(e)
        print("Debe registrar nuevamente al profesor")

# Agregar estudiantes al curso
def add_student():
    try:
        print("Registrar alumno")
        poo_student_first_name = input("Ingresar el nombre del alumno: ")
        poo_student_last_name = input("Ingresar el apellido del alumno: ")
        poo_student_id = input("Ingresar el codigo para el alumno: ")
        poo_student = Student(poo_student_id, poo_student_first_name, poo_student_last_name)
        poo_student_email = input("Ingresar el email del alumno: ")
        poo_student.set_email(poo_student_email)
        poo_student_registration_date = input("Ingresar la fecha de matricula (dd/MM/yyyy): ")
        poo_student.set_registration_date(poo_student_registration_date)
        global poo_course
        poo_course.add_student(poo_student)
    except ValueError as e:
        print(e)
        print("Debe registrar nuevamente al alumno")

# Eliminar un estudiante del curso
def remove_student():
    try:
        print("Eliminar alumno")
        global poo_course
        poo_student_email = input("Ingresar el email del alumno: ")
        item = poo_course.searc_student_by_email(poo_student_email)
        if item == None:
            print("ERROR: El alumno no existe")
        else:
            poo_course.remove_student(item.get_id())
    except ValueError as e:
        print(e)
        print("Debe repetir el proceso de remover al alumno")

# Mostrar el detalle del curso
def show_course_detail():
    global poo_course
    print("Detalle del curso")
    print(f"Codigo curso: {poo_course.get_id()}")
    print(f"Nombre profesor {poo_course.get_teacher().first_name} {poo_course.get_teacher().last_name}")
    print("Lista de alumnos")
    item: Student
    for item in poo_course.get_students():
        print(f"Nombre:\t{item.first_name} {item.last_name}\tEmail:\t{item.get_email()}\tFecha Matricula:\t{item.get_registration_date()}")

# Programa principal con un menu para mantener el funcionamiento
def main_menu():
    show_menu = True
    while show_menu:
        print("Programa Principal")
        print("1.- Ingresar profesor al curso")
        print("2.- Ingresar alumno al curso")
        print("3.- Remover alumno del curso")
        print("4.- Mostrar detalle del curso")
        print("5.- Salir")
        option = input("Ingrese su opcion: ")
        if option == "1":
            add_teacher()
        elif option == "2":
            add_student()
        elif option == "3":
            remove_student()
        elif option == "4":
            show_course_detail()
        elif option == "5":
            show_menu = False

# Llamada al programa principal
main_menu()