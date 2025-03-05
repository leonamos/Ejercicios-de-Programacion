#un cajero automatico
usuario = list()

usuario = list("amosleon") # string str
usuario.append("1234")      # string str
usuario.append(1000)        # int

recibo = list()
recibo.append(["123", 600])
recibo.append(["124", 845])
recibo.append(["125", 67])
recibo.append(["126", 500])
recibo.append(["127", 100])
recibo.append(["128", 1000])




acciones = list()
acciones.append("depositar")
acciones.append("pago de recibo")
acciones.append("retirar")


usuario2 = list("leon")     # string str
usuario2.append("12345")    # string str
usuario2.append(1500)       # int

def registrar():
    UsuarioRegistrado = list()
    usuarioC = input("Ingrese su nombre: ")
    UsuarioRegistrado.append("Ingrese su password: ")

    if "usuarioC" == usuario[0] and UsuarioRegistrado[0] == usuario[1]:
        print("Bienvenido al cajero automatico")
    else:
        print("Usuario o contraseña incorrectos")
        return registrar()