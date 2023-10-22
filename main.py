import clases as clase
import os
op = ""

def mostrar_menu():
    os.system("cls")
    print("Bienvenido al sistema del campus virtual\n\nSeleccione una opción del menú:")
    print("1.Ingresar como alumno\n2.Ingresar como profesor\n3.Ver cursos\n4.Salir")
    
while op !=4:
    mostrar_menu()
    op = input("")
    if  op.isdigit():
        op=int(op)
        if op >= 1 and op <= 4:
            if op == 1:
                os.system("cls")
                ingreso = clase.Estudiante.validar_credenciales(clase.lista_estudiantes)
                if ingreso:
                    op_menu_alumno = ""
                    
                    while op_menu_alumno != "3":
                        os.system("cls")    
                        op_menu_alumno = (input("Seleccione una opcion:\n1-Matricularse a un curso\n2-Ver curso\n3-Volver al menu principal\n"))
                        if op_menu_alumno == "1" and op_menu_alumno.isdigit():
                            clase.Estudiante.matricular_en_curso(ingreso)
                        elif op_menu_alumno == "2" and op_menu_alumno.isdigit():
                            clase.Estudiante.ver_cursos(ingreso)
                        elif op_menu_alumno == "3" and op_menu_alumno.isdigit():
                            pass
                        else:
                            print("Opción invalida.")
                            input("Pulse cualquier tecla para volver a intentarlo...")

            elif op==2:
                os.system("cls")
                ingreso = clase.Profesor.validar_credenciales(clase.lista_profesores)
                if ingreso:
                    op_menu_profesor = ""
                    while op_menu_profesor != "3":
                        os.system("cls")
                        op_menu_profesor = (input("Seleccione una opcion:\n1-Dictar curso\n2-Ver curso\n3-Volver al menu principal\n"))
                        if op_menu_profesor == "1" and op_menu_profesor.isdigit():
                            clase.Profesor.dictar_curso(ingreso)
                        elif op_menu_profesor == "2" and op_menu_profesor.isdigit():
                            clase.Profesor.ver_cursos(ingreso)
                        elif op_menu_profesor == "3" and op_menu_profesor.isdigit():
                            pass
                        else:
                            print("Opción inválida")

            elif op==3: 
                os.system("cls")
                print("Aquí esta la lista de cursos disponibles del campus virtual:\n")
                for i in range(len(clase.lista_cursos)):
                    print(clase.lista_cursos[i])
                input("\nPresione cualquier tecla para volver al menú...")

            elif op==4:
                pass
        else:
            input("Valor ingresado inválido, pulse un botón para intentarlo nuevamente...")
    else:
        input("El valor ingresado es inválido, pulse un botón para intentarlo nuevamente...")