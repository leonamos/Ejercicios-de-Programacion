def calculadora ():
    print("seleccione una accion")
    print("seleccione una opcion")
    
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.division")
    print("5. salir")

    opcion = input("ingrese la opcion : ")
    
    if opcion in ("1", "2", "3", "4"):
        num1 = float(input("ingrese el primer numero: "))
        num2 = float(input("ingrese el segundo numero: "))
        
        