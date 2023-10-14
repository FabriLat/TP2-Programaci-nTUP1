import clases as clase
import os
op = int()
print("Bienvenido al sistema del campus virtual\n\nSeleccione una opción del menú:")
def mostrar_menu():
    print("1.Ingresar como alumno\n2.Ingresar como profesor\n3.Ver cursos\n4.Salir")
while op !=4:
    mostrar_menu()
    op = int(input(""))
    if op >= 1 and op <= 4:
        if op ==1:
            os.system("cls")
            clase.Estudiante.validar_credenciales(clase.lista_estudiantes)

        elif op==2:
            os.system("cls")
            clase.Profesor.validar_credenciales(clase.lista_profesores)
        elif op==3: 
            pass
        elif op==4:
            pass
    else:
        print("Valor ingresado inválido")