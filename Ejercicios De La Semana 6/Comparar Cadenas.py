def comparar_cadenas():
    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    
    if cadena1 == cadena2:
        print("Las cadenas son iguales.")
    else:
        print("Las cadenas son diferentes.")
        if cadena1 > cadena2:
            print(f'"{cadena1}" es mayor en orden alfabético que "{cadena2}".')
        else:
            print(f'"{cadena2}" es mayor en orden alfabético que "{cadena1}".')

comparar_cadenas()