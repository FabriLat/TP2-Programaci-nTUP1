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
        if op == 1:
            os.system("cls")
            ingreso = clase.Estudiante.validar_credenciales(clase.lista_estudiantes)
            if ingreso:
                op = int(input("Seleccione una opcion:\n1-Matricularse a un curso\n2-Ver curso\n3-Volver al menu principal\n"))
                if op == 1:
                    clase.Estudiante.matricular_en_curso(ingreso)
                elif op == 2:
                    pass
                elif op == 3:
                    pass
                else:
                    print("Opción invalida.")



        elif op==2:
            os.system("cls")
            clase.Profesor.validar_credenciales(clase.lista_profesores)
        elif op==3: 
            pass
        elif op==4:
            pass
    else:
        print("Valor ingresado inválido")