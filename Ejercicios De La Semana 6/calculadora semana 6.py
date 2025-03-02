def calculadora ():
    print("seleccione una accion")
    print("seleccione una opcion")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5. salir")

    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        
        if opcion == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se `puede dividir por cero.")
    else:
        print("Opcion no valida. Intente de nuevo.")
        
calculadora()



