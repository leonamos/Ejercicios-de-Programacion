import random

def numero_aleatorio():
    print("Generador de Número Aleatorio")
    num = random.randint(1, 100)
    print(f"Número generado: {num}")

numero_aleatorio()