### Clases y Objetos 
# Una clase es una plantilla para crear objetos. Un objeto es una instancia de una clase.

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."    

# Crear un objeto (instancia de la clase)
persona1 = persona("Amós", 18)
print(persona1.saludar()) # Salida: Hola, mi nombre es Juan y tengo 25 años.


### Encapsulamiento
# Permite restringir el acceso a los atributos y métodos de una clase usando modificadores de acceso.

class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado (dos guiones bajos)
        
    def depositar(self, cantidad):
        self.__saldo += cantidad
            
    def obtener_saldo(self):
        return self.__saldo   # Método para acceder al atributo privado

# Uso
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print(cuenta.obtener_saldo())   # Salida: 1500


### Herencia
# Permite que una clase herede atributos y métodos de otra.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def sonido(self):
        return "Hace un sonido"
    
# Clase Perro hereda de Animal 
class Perro(Animal):
    def sonido(self):
        return "Ladra"
    
# Uso 
perro = Perro("Bobby")
print(perro.nombre)   # Salida: Bobby
print(perro.sonido()) # Salida: Ladra



### Herencia
# Permite que una clase herede atributos y métodos de otra.

class Gato:
    def sonido(self):
        return "Maulla"    

class Perro:
    def sonido(self):
        return "Ladra"
    
# Uso de polimorfismo
def hacer_sonido(animal):
    print (animal.sonido())
    
gato = Gato()
perro = Perro()

hacer_sonido(gato)  # Salida: Maulla
hacer_sonido(perro) # Salida: Ladra