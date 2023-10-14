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
            email=input("Ingrese su mail: ")
            i=0
            while i < len(clase.lista_estudiantes):
                if clase.lista_estudiantes[i].email == email:
                    clase.Estudiante.validar_credenciales(clase.lista_estudiantes[i])
                    break
                else:
                    i+=1
                    if i == len(clase.lista_estudiantes):
                        print("Su usuario no existe, debe darse de alta en el alumnado.")
                        break
                

        elif op==2:
            pass
        elif op==3:
            pass
        elif op==4:
            pass
    else:
        print("Valor ingresado inválido")