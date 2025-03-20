Algoritmo Bucle 
	
	
	
	
	
	registro("hola")
	
FinAlgoritmo

	Funcion registro (NJ)
		re = Falso
		
		Escribir "correo"
		Leer correo
		
		Escribir "password"
		Leer password
		
		Mientras re
			si correo <> "Holamundo"
				Escribir "Error detectado"
			FinSi
			si password <> "1234"
				Escribir "Error detectado"
			FinSi
			
			si correo = "holamundo" y password = "1234"
				re = Falso
				Escribir "Bienvenido"
			FinSi
		FinMientras
		registro("hola")
FinFuncion

