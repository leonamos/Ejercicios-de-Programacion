Algoritmo EjemploFor
	resultado(20)
FinAlgoritmo


Funcion resultado (numero)
	
	total = 0
	
	para i = 0 Hasta numero
		valorActual = total
		total = i + total
		si total mod 2 <> 0
			Escribir "La suma es", i , " + " , valorActial
		FinSi
	FinPara
	Escribir "La suma es", total
FinFuncion
'public Funcion tipo de dato devuelto nombre ()