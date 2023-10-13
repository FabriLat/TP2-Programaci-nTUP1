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
        super.__init__(self,nombre,apellido,email,contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso

    def dictar_curso(self):
        pass


class Estudiante(Persona):
    def __init__(self,nombre,apellido,email,contrasenia,legajo,anio_inscripcion_carrera):
        super.__init__(self,nombre,apellido,email,contrasenia)
        self.legajo=legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera


    def matricular_en_curso(self):
        pass


    
class Curso(Profesor,Estudiante):
    def __init__(self,nombre,apellido,email,contrasenia,titulo,anio_egreso,legajo,anio_inscripcion_carrera):
        Persona.__init__(self,nombre,apellido,email,contrasenia)
        Profesor.__init__(self,titulo,anio_egreso)
        Estudiante.__init__(self,legajo,anio_inscripcion_carrera)
