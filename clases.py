from abc import ABC,abstractmethod
import os
import random

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
        self.mis_cursos = []

    def __str__(self):
        return f"Nombre:{self.nombre} {self.apellido}"

    def dictar_curso(self):
        pass

    def validar_credenciales(self):
        os.system("cls")
        email=input("Ingrese su mail: ")
        password = input("Ingrese su contraseña: ")
        i=0
        while i < len(lista_profesores):
            if lista_profesores[i].email == email:
                if lista_profesores[i].contrasenia == password:
                    print("Logueado con exito.")
                    return True
                else:
                    print("Email o contraseña invalido.")
                    return False
            else:
                i+=1
                if i == len(lista_profesores):
                    print("Su usuario no existe, debe darse de alta en el alumnado.")
                    return False

class Estudiante(Persona):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mis_cursos = []
        
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"
    
    def matricular_en_curso(self):
        os.system("cls")
        print("Seleccione el curso para matricularse:\n")
        for curso in range(len(lista_cursos)):
            print(f"{curso+1}. {lista_cursos[curso]}")
        seleccionado = int(input(""))
        while seleccionado < 0 or seleccionado > 8:
            if seleccionado < 0 or seleccionado > 8:
                seleccionado = int(input("Opcion invalida, vuelve a seleccionarla."))

        if seleccionado == 1:
            seleccionado = "Arquitectura de software"
        elif seleccionado ==2:
             seleccionado = "Ingles 1"
        elif seleccionado ==3:
             seleccionado = "Ingles 2"
        elif seleccionado ==4:
             seleccionado = "Laboratorio 1"
        elif seleccionado ==5:
             seleccionado = "Laboratorio 2"
        elif seleccionado ==6:
             seleccionado = "Metodologia de la investigacion"
        elif seleccionado ==7:
             seleccionado = "Programacion 1"
        elif seleccionado ==8:
             seleccionado = "Programacion 2" 
        else:
            print("Opción inválida.")

        if seleccionado in self.mis_cursos:
            print("Usted ya está inscripto en este curso.")
        else:
            self.mis_cursos.append(seleccionado)
            print(f"{self.nombre} está ahora inscripto en {seleccionado}")
        input("Pulse cualquier tecla para volver al menú...")

    def ver_cursos(self):
        os.system("cls")
        print(f"{self.nombre} está inscripto en: ")
        for curso in self.mis_cursos:
            print(f"- {curso}")
        input("Presione cualquier tecla para continuar...")


    def validar_credenciales(self):
            email=input("Ingrese su mail: ")
            password = input("Ingrese su contraseña: ")
            i=0
            while i < len(lista_estudiantes):
                if lista_estudiantes[i].email == email:
                    if lista_estudiantes[i].contrasenia == password:
                        os.system("cls")
                        print("Logueado con exito.\n")
                        input("Presione cualquier telca para continuar...")
                        return lista_estudiantes[i]
                    else:
                        print("Email o contraseña invalido.")
                        return False
                else:
                    i+=1
                    if i == len(lista_estudiantes):
                        print("Su usuario no existe, debe darse de alta en el alumnado.")
                        return False
                                 
class Curso:
    def __init__(self,nombre,contrasenia_matriculacion):
        self.nombre = nombre
        self.contrasenia_matriculacion = contrasenia_matriculacion

    def __str__(self):
        return f"Curso: {self.nombre}"

    def generar_contrasenia():
        letras = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(3))
        numeros = ''.join(random.choice('0123456789') for i in range(2))
        return letras+numeros


lista_estudiantes=[]
lista_profesores=[]
lista_cursos=[]
alumno1=Estudiante("Pedro","Rogriguez","Pedro@gmail.com","pedro123",123,2023)
alumno2=Estudiante("Leo","Messi","Leo@gmail.com","leo123",456,2022)
alumno3=Estudiante("Enzo","Fernandez","Enzo@gmail.com","enzo123",789,2021)

lista_estudiantes.append(alumno1)
lista_estudiantes.append(alumno2)
lista_estudiantes.append(alumno3)
profesor1=Profesor("Carlitos","Niell","carlitos@gmail.com","carlitos123","Ingeniero",1990)
profesor2=Profesor("Pedro","Lopez","pedrito@gmail.com","pedrito123","ingeniero",1980)
lista_profesores.append(profesor1)
lista_profesores.append(profesor2)

#agregar contraseñas de los cursos
curso1=Curso("Arquitectura de software","")
curso2=Curso("Ingles 1","")
curso3=Curso("Ingles 2","")
curso4=Curso("Estadistica","")
curso4=Curso("Laboratorio 1","")
curso5=Curso("Laboratorio 2","")
curso6=Curso("Metodologia","")
curso7=Curso("Programacion 1","")
curso8=Curso("Programacion 2","")
lista_cursos.append(curso1)
lista_cursos.append(curso2)
lista_cursos.append(curso3)
lista_cursos.append(curso4)
lista_cursos.append(curso5)
lista_cursos.append(curso6)
lista_cursos.append(curso7)
lista_cursos.append(curso8)