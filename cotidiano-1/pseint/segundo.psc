Algoritmo sin_titulo
	contador = 0
	suma = 0
	num = 0
	
	Mientras contador <= 100 Hacer
		si num mod 2 == 0 Entonces
			suma = suma + num
		FinSi
		
		num = num + 1
		contador = contador + 1
	FinMientras
	
	escribir suma
FinAlgoritmo
