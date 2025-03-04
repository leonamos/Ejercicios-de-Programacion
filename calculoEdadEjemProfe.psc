Algoritmo calculoEdadEjemProfe
	
	definir nacimiento, actual, total como entero
	
	// and  verdadero + verdadero = verdadero 
	//      verdadero + false = false 
	
	suma = 5
	suma2 = 7
	
	//2  es mayor a  10   and  4 < 10
	
	si 2 > 10 & 4< 10 
		Escribir (" and verdad")
	sino 
		Escribir ("and falso")
	FinSi
	
	// or   verdadero + falso = verdadero 
	//		falso + falso = falso
	
	si 12 > 10 o  4 < 10 
		Escribir ("or verdad")
	sino 
		Escribir ("or falso")
	FinSi
	
	
	edad = 0
	nacimiento = 0
	actual = 0
	
	escribir "Ingrese ao de nacimineto"
	leer  nacimiento
	
	actual = 2025
	
	// que el a;o que ingrese suma mayor a 0
	// sea mayor a fecha acrual -100
	si nacimiento > 0 Y  actual - 100 > 1900
		edad = actual - nacimiento
		Escribir  " tiene " , edad , "a;os"
	SiNo
		Escribir  " Error en la edad"
	FinSi
	
FinAlgoritmo

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
FinAlgoritmo
