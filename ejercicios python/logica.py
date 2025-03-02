#un cajero automatico

usuario = list()

usuario = list("amos leon") # string str
usuario.append("12345")      # string str
usuario.append(1000)        # int

recibo = list()
recibo.append(["123", 600])
recibo.append(["456", 800])
recibo.append(["789", 1000])
recibo.append(["123", 2000])
recibo.append(["456", 3000])
recibo.append(["789", 4000])

acciones = list()
acciones.append("depositar")
acciones.append("pago de recibo")
acciones.append("retirar")

usuario2 = list()
usuario2 = list("leon")     # string str
usuario2.append("12345")    # string str
usuario2.append(1500)       # int

def registrar():
    usuarioRegistrado = list()
    usuarioC = input("Ingrese su nombre: ")
    usuarioRegistrado = input("Ingrese su password: ")

    if usuarioC == usuario[0] and usuarioRegistrado[0] == usuario[1]:
        print("Bienvenido al cajero automatico")
    else:
        print("Usuario o contraseña incorrectos")
        return registrar()