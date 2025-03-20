import math

def perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = 23
resultado = perimetro_circulo(radio)
print(f"El perímetro del círculo con radio {radio} es {resultado:.2f} unidades")