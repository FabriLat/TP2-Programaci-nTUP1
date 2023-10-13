from abc import ABC,abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,apellido,email,contrasenia):
        self.nombre = nombre
        self.apellido=apellido
        self.email=email
        self.contrasenia=contrasenia

    @abstractclassmethod
    def __str__(self) -> str:
        pass
    
    @abstractclassmethod
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
    def __init__(self,nombre,apellido,email,contrasenia,legajo,anio_inscripcion_carrera):
        super().__init__(nombre,apellido,email,contrasenia)
        self.legajo=legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"

    def matricular_en_curso(self):
        pass
    
    def validar_credenciales(self):
        pass







class Curso(Profesor,Estudiante):
    def __init__(self,nombre,apellido,email,contrasenia,titulo,anio_egreso,legajo,anio_inscripcion_carrera):
        Persona.__init__(self,nombre,apellido,email,contrasenia)
        Profesor.__init__(self,titulo,anio_egreso)
        Estudiante.__init__(self,legajo,anio_inscripcion_carrera)

    def generar_contrasenia(self):
        pass



alumno1=Estudiante("Pedro","Rogriguez","Pedro@gmail.com","pedro123",321,2023)

profesor1=Profesor("Carlitos","Niell","carlitos@gmail.com","carlitos123","Ingeniero",1990)
print(profesor1)