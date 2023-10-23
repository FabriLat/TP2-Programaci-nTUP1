from abc import ABC,abstractmethod
import os
import random

class Usuario(ABC):
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

class Profesor(Usuario):
    def __init__(self,nombre,apellido,email,contrasenia,titulo,anio_egreso):
        super().__init__(nombre,apellido,email,contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso
        self.mis_cursos = []

    def __str__(self):
        return f"Nombre:{self.nombre} {self.apellido}"

    def dictar_curso(self):
        os.system("cls")

        nombre_curso = input("Ingrese el nombre del curso a dictar: ")
        while len(nombre_curso) == 0:
            if len(nombre_curso) == 0:
                nombre_curso = input("Error, ingrese un nombre válido: ")
        nombre_curso.capitalize()
        clave_curso = input("Ingrese la clave de matriculación: ")
        while len(clave_curso) < 2 or len(clave_curso) > 6:
            if len(clave_curso) < 2 or len(clave_curso) > 6:
                clave_curso = input("Error, ingrese un valor alfanumerico entre 3-5 caracteres")

        nuevo_curso = Curso(nombre_curso,clave_curso)
        if len(self.mis_cursos) == 0:
            lista_cursos.append(nuevo_curso)
            self.mis_cursos.append(nuevo_curso)
            print(f"Usted ha empezado a dictar el curso {nuevo_curso.nombre}")
            input("Pulse cualquier tecla para continuar...")
            return ""


        for curso in range(len(self.mis_cursos)):
            if nuevo_curso.nombre == self.mis_cursos[curso].nombre:
                print("Usted ya está a cargo de este curso")
                input("Pulse cualquier tecla para volver al menú...")  
                return ""

        lista_cursos.append(nuevo_curso)
        self.mis_cursos.append(nuevo_curso)
        os.system("cls")
        print(f"Usted ha empezado a dictar el curso {nuevo_curso.nombre}")
        input("Pulse cualquier tecla para continuar...")
        return ""
                
    def validar_credenciales(self):
        os.system("cls")
        email=input("Ingrese su mail: ")
        password = input("Ingrese su contraseña: ")
        i=0
        while i < len(lista_profesores):
            if lista_profesores[i].email == email:
                if lista_profesores[i].contrasenia == password:
                    print("Logueado con exito.")
                    input("Presione cualquier tecla para continuar...")
                    return lista_profesores[i]
                else:
                    print("Email o contraseña invalido.")
                    input("Presione cualquier tecla para volver al menú...")
                    return False
            else:
                i+=1
                if i == len(lista_profesores):
                    print("Su usuario no existe, debe darse de alta en el alumnado.\n")
                    alta = input("Ingrese 'admin' para darse de alta u otro caracter para volver al menú: ")

        
        if alta == "admin":
            os.system("cls")
            print("--Alta de profesores--\n")
            nombre = input("Ingrese nombre: ")
            apellido = input("Ingrese apellido: ")
            mail = input("Ingrese mail: ")
            contrasenia = input("Ingrese contraseña: ")
            titulo = input("Ingrese su titulo: ")
            anio_egreso = input("Ingrese su año de egreso: ")
            nuevo_profesor = Profesor(nombre,apellido,mail,contrasenia,titulo,anio_egreso)
            lista_profesores.append(nuevo_profesor)
            input("Profesor registrado exitosamente...")
        else:
            return ""


                
    def ver_cursos(self):
        os.system("cls")
        if len(self.mis_cursos) > 0:
            print("Los cursos que usted tiene a cargo son: ")
            for curso in range(len(self.mis_cursos)):
                print(f"- {self.mis_cursos[curso]}({self.mis_cursos[curso].contrasenia_matriculacion})")
            input("\nPulse cualquier tecla para volver al menú...")
        else:
            print("Usted no tiene cursos a cargo suyo.")
            input("\nPulse cualquier tecla para volver al menú...")

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mis_cursos = []
        
    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"
    
    def matricular_en_curso(self):
        os.system("cls")
        bandera = False
        if len(lista_cursos) == 0:
            print("No hay cursos disponibles")
            input("Pulse cualquier tecla para volver al menu...")
            return ""
        
        print("Seleccione el curso para matricularse:\n")
        for curso in range(len(lista_cursos)):
            print(f"{curso+1}. {lista_cursos[curso]}")

        while True:
            seleccion = input("")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 0 < seleccion <= len(lista_cursos):
                    break
            print("Error, seleccione un valor válido.")
        nombre = lista_cursos[seleccion - 1].nombre
        clave = input("Ingrese clave de matriculación: ")

        for claves in range(len(lista_cursos)):
            if clave == lista_cursos[claves].contrasenia_matriculacion and nombre == lista_cursos[claves].nombre:
                bandera = True
                seleccion = lista_cursos[seleccion - 1]
       
        if seleccion not in self.mis_cursos and bandera == True:
            self.mis_cursos.append(seleccion)
            os.system("cls")
            print(f"{self.nombre} se ha inscripto en el {seleccion}")
            input("Pulse cualquier tecla para continuar...")
        elif bandera == False:
            print("Error, clave incorrecta.")
            input("Pulse cualquier tecla para volver al menú...")
        else:
            print(f"{self.nombre} ya está inscripto en este curso")
            input("Pulse cualquier tecla para volver al menú...")


    def desmatricular_curso(self):
        os.system("cls")
        if len(self.mis_cursos) == 0:
            print("Usted no está matriculado en ningun curso.")
            input("Pulse cualquier tecla para volver al menú...")
            return ""
        print("Seleccione el curso para desmatricularse:\n")
        for curso in range(len(self.mis_cursos)):
            print(f"{curso+1}. {self.mis_cursos[curso]}")

        while True:
            seleccion = input("")
            if seleccion.isdigit():
                seleccion = int(seleccion)
                if 0 < seleccion <= len(self.mis_cursos):
                    break
                else:
                    print("Valor ingresado inválido, intente nuevamente: ")
        eliminado = self.mis_cursos.pop(seleccion-1)   
        print(f"Usted se ha desmatriculado de {eliminado}")
        input("Presione cualquier tecla para volver al menú...")
        
        



    def ver_cursos(self):
        os.system("cls")
        if len(self.mis_cursos) == 0:
            print(f"{self.nombre} no está inscripto en ningun curso")
            input("Pulse cualquier boton para continuar...")
            return ""
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
                        print("Email o contraseña invalido.\n")
                        input("Presione cualquier telca para volver al menú...")
                        return False
                else:
                    i+=1
                    if i == len(lista_estudiantes):
                        print("Su usuario no existe, debe darse de alta en el alumnado.\n")
                        input("Presione cualquier telca para volver al menú...")
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
    

class Archivo:
    def __init__(self,nombre,fecha,formato):
        self.nombre = nombre
        self.fecha = fecha
        self.formato = formato

    def __str__(self) -> str:
        return f"Archivo: {self.nombre}, fecha: {self.fecha}, formato: {self.formato}"


class Carrera:
    def __init__(self,nombre,cant_anios):
        self.nombre = nombre
        self.cant_anios = cant_anios

    def __str__(self):
        return f"carrera:{self.nombre}"

    def get_cantidad_materias(self):
        pass


lista_estudiantes=[]
lista_profesores=[]
lista_cursos=[]
alumno=Estudiante("Pedro","Rogriguez","Pedro@gmail.com","pedro123",123,2023)
lista_estudiantes.append(alumno)
alumno=Estudiante("Leo","Messi","Leo@gmail.com","leo123",456,2022)
lista_estudiantes.append(alumno)
alumno=Estudiante("Enzo","Fernandez","Enzo@gmail.com","enzo123",789,2021)
lista_estudiantes.append(alumno)

profesor=Profesor("Carlitos","Niell","carlitos@gmail.com","carlitos123","Ingeniero",1990)
lista_profesores.append(profesor)
profesor=Profesor("Pedro","Lopez","pedrito@gmail.com","pedrito123","Ingeniero",1980)
lista_profesores.append(profesor)

