import random

def juego_adivinanza():
    # Generamos un número secreto entre 1 y 50
    numero_secreto = random.randint(1, 50)

    # Máximo de intentos
    intentos_max = 5
    intentos = 0

    print("¡Bienvenido al juego de adivinanza!")
    print("Debes adivinar un número entre 1 y 50.")
    print("Tienes un máximo de 5 intentos. Escribe 'salir' para terminar en cualquier momento.\n")
    # Bucle principal del juego
    while intentos < intentos_max:
        respuesta = input("Ingresa un número (o 'salir'): ")

        # Verificamos si el usuario desea salir
        if respuesta.lower() == "salir":
            print("Has salido del juego. ¡Hasta la próxima!")
            return  # Salimos de la función

        # Validamos que la entrada sea un número
        if not respuesta.isdigit():
            print("Entrada inválida. Por favor, ingresa un número o 'salir'.\n")
            continue

        # Convertimos la respuesta a entero
        intento = int(respuesta)

        # Validamos que el número esté dentro del rango
        if intento < 1 or intento > 50:
            print("Por favor, ingresa un número entre 1 y 50.\n")
            continue

        intentos += 1  # Aumentamos el contador de intentos

        # Comparamos el intento con el número secreto
        if intento < numero_secreto:
            print("Demasiado bajo. Intenta de nuevo.\n")
        elif intento > numero_secreto:
            print("Demasiado alto. Intenta de nuevo.\n")
        else:
            # Si el usuario acierta
            print(f"¡Felicidades! Adivinaste el número secreto en {intentos} intento(s).")
            return  # Terminamos el juego

    # Si se llegan a agotar los intentos sin adivinar
    print(f"Se han agotado los {intentos_max} intentos. El número secreto era {numero_secreto}.")

# Llamamos a la función para iniciar el juego
juego_adivinanza()