#un cajero automatico

usuarios = {  # Diccionario para almacenar múltiples usuarios
    "amosleon": "1234",
    "leon": "12345",
    "amos": "123456"
}

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

acciones = list()
acciones.append("depositar")
acciones.append("pago de recibo")
acciones.append("retiro")

usuario2 = list()
usuario2.append("leon")     # string str
usuario2.append("12345")    # string str
usuario2.append(1500)       # int



def registrar():
    usuarioC = input("Ingrese su nombre: ")
    usuarioRegistrado = input("Ingrese su password: ")

    if usuarioC in usuarios and usuarios[usuarioC] == usuarioRegistrado:
        print("Bienvenido al cajero automático")
    else:
        print("Usuario o contraseña incorrectos")

registrar()  # Ejecutar la función

