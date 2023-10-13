import clases as clase
op = int()
print("Bienvenido al sistema del campus virtual\n\nSeleccione una opción del menú:")
def mostrar_menu():
    print("1.Ingresar como alumno\n2.Ingresar como profesor\n3.Ver cursos\n4.Salir")



while op !=4:
    mostrar_menu()
    op = int(input(""))
    if op >= 1 and op <= 4:
        if op ==1:
            pass
        elif op==2:
            pass
        elif op==3:
            pass
        elif op==4:
            pass
    else:
        print("Valor ingresado inválido")