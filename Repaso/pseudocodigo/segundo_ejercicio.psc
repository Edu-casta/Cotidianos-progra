Algoritmo segundo_ejercicio
	Limpiar Pantalla
	Escribir "Ingrese tres números"
	leer n1, n2, n3
	
	Escribir "Ingrese el operador (+, -, *, /, prom)"
	leer op
	
	Segun op Hacer
		"+":
			Escribir n1 + n2 + n3
		"-":
			Escribir n1 - n2 - n3
		"*":
			Escribir n1 * n2 * n3
		"/":
			si n2 == 0 o n3 == 0 Entonces
				Escribir "Error"
			FinSi
			
			Escribir n1 / n2 / n3
		"prom":
			Escribir (n1 + n2 + n3)/3
		De Otro Modo:
			Escribir "ERROR"
	Fin Segun
FinAlgoritmo
