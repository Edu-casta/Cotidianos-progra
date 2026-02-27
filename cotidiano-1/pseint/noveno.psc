Algoritmo sin_titulo
	i = 0
	neg = 0
	pos = 0
	num = 1
	
	Mientras num <> 0
		num = 0
		
		Escribir "Ingrese un número"
		leer num
		
		si num = 0 Entonces
			Escribir "Gracias por usar"
		FinSi
		
		si num > 0 Entonces
			pos = pos + 1
		sino 
			pos = pos - 1
		FinSi
	FinMientras
	Escribir pos," ",neg
FinAlgoritmo
