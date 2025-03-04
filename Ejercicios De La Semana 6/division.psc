Algoritmo division 
	
	//Escribe un programa que lea un numero y determine si es par o impar.
	
	a = 0
	b = 0
	c = 0
	r = Falso
		
	Escribir "ingrese el numero a dividir"
	leer a
		
	Escribir "ingrese el numero con el que se va a dividir"
	Leer b
		
	c = a + b
	t = c mod 2
		
	 si t == 0 Entonces
		 r = Verdadero
		 Escribir t
	 FinSi
		
	 si t <> 0 Entonces
		r = Falso
		Escribir t
	 FinSi
	Escribir "La respuesta es ", r
FinAlgoritmo
