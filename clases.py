from abc import ABC,abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self,nombre,apellido,email,contrasenia):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.contrasenia=contrasenia

    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def validar_credenciales(self) -> bool :
        pass

class Profesor(Persona):
    def __init__(self,nombre,apellido,email,contrasenia,titulo,anio_egreso):
        super().__init__(nombre,apellido,email,contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def __str__(self):
        return f"Nombre:{self.nombre} {self.apellido}"

    def dictar_curso(self):
        pass

    def validar_credenciales(self):
        pass

class Estudiante(Persona):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

    def matricular_en_curso(self):
        pass
    
    def validar_credenciales(self):
        password = input("Ingrese su contraseña: ")
        if self.contrasenia == password:
            print("Logueado con exito")
        else:
            print("Error, mail o contraseña inválido")
# 
class Curso:
    def __init__(self,nombre,profesor):
        self.nombre = nombre
        self.profesor = profesor

    def __str__(self):
        return f"Curso: {self.nombre} a cargo del profesor {self.profesor}"

    def generar_contrasenia(self):
        pass

lista_estudiantes=[]
alumno1=Estudiante("Pedro","Rogriguez","Pedro@gmail.com","pedro123",123,2023)
alumno2=Estudiante("Leo","Messi","Leo@gmail.com","leo123",456,2022)
alumno3=Estudiante("Enzo","Fernandez","Enzo@gmail.com","enzo123",789,2021)
lista_estudiantes.append(alumno1)
lista_estudiantes.append(alumno2)
lista_estudiantes.append(alumno3)
profesor1=Profesor("Carlitos","Niell","carlitos@gmail.com","carlitos123","Ingeniero",1990)
profesor2=("Pedro","Lopez","pedrito@gmail.com","pedrito123","ingeniero",1980)
curso1=Curso("Programacion 1",profesor1.nombre)

