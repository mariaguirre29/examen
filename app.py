from utilidades import menu, asignar_sueldos, clasificar_sueldos, importe_csv




while True:
    try:
        menu()
        opcion = int(input("ingrese la opcion que necesite: "))
        if opcion == 1:
            asignar_sueldos()
            
        elif opcion == 2:
           clasificar_sueldos()
           
        elif opcion == 3:
            print("hola")
            
        elif opcion == 4:
            importe_csv()
            print("Usted ha salido del programa. ")
            
        else:
            print("Opcion ivalida! intente nuevamente")
            
    except ValueError:
        print("Dato invalido! solo puedes ingresar numeros\n")
 
    except ZeroDivisionError:
        print("Dato invalido! No puedes ingresar 0\n")