import clases as clase
import os
op = int()

def mostrar_menu():
    os.system("cls")
    print("Bienvenido al sistema del campus virtual\n\nSeleccione una opción del menú:")
    print("1.Ingresar como alumno\n2.Ingresar como profesor\n3.Ver cursos\n4.Salir")
    
while op !=4:
    mostrar_menu()
    op = int(input(""))
    if op >= 1 and op <= 4:
        if op == 1:
            os.system("cls")
            ingreso = clase.Estudiante.validar_credenciales(clase.lista_estudiantes)
            if ingreso:
                op_menu_alumno = int()
                while op_menu_alumno != 3:
                    os.system("cls")
                    op_menu_alumno = int(input("Seleccione una opcion:\n1-Matricularse a un curso\n2-Ver curso\n3-Volver al menu principal\n"))
                    if op_menu_alumno == 1:
                        clase.Estudiante.matricular_en_curso(ingreso)
                    elif op_menu_alumno == 2:
                        clase.Estudiante.ver_cursos(ingreso)
                    elif op_menu_alumno == 3:
                        pass
                    else:
                        print("Opción invalida.")

        elif op==2:
            os.system("cls")
            ingreso = clase.Profesor.validar_credenciales(clase.lista_profesores)
            if ingreso:
                op_menu_profesor = int()
                while op_menu_profesor != 3:
                    os.system("cls")
                    op_menu_profesor = int(input("Seleccione una opcion:\n1-Dictar curso\n2-Ver curso\n3-Volver al menu principal\n"))
                    if op_menu_profesor == 1:
                        clase.Profesor.dictar_curso(ingreso)
                    elif op_menu_profesor == 2:
                        clase.Profesor.ver_cursos(ingreso)
                    elif op_menu_profesor == 3:
                        pass
                    else:
                        print("Opción invalida.")

        elif op==3: 
            pass
        elif op==4:
            pass
    else:
        print("Valor ingresado inválido")