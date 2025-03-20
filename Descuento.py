compra = float(input("Ingrese el valor de la compra: "))
valor = 0.5 if compra <= 50 else 1

def mostrar (compra):
    if compra < 50:
        print("Total sin descuento", compra)
        print("Descuento: no aplica")
        print("Total a pagar", compra)
    else:
        descuento = compra * descuento
        total = compra - descuento
        print("Total sin descuento", compra)
        print("Descuento:", descuento)
        print("Total a pagar", total)
        print("Gracias por su compra")

def mostrar(compra, descuento):
    if compra < 50:
        print("Total sin descuento", compra)
        print("Descuento: no aplica")
        print("Total a pagar", compra)
    else:
        descuento = compra * descuento
        total = compra - descuento
        print("Total sin descuento", compra)
        print("Descuento:", descuento)
        print("Total a pagar", total)

if compra >= 50 and compra < 100:
    descuento = 0.05

if compra >= 100 and compra < 100:
    descuento = 0.10

if compra >= 100 and compra < 200:
    descuento = 0.12

if compra >= 200 and compra < 1000:
    descuento = 0.2
mostrar(compra, descuento)
print("Gracias por su compra")