Algoritmo tercer_ejercicio
	Escribir "Ingrese su calificación: "
	leer calificacion
	
	si calificacion >= 90 Entonces
		nota = "A"
		sino si calificacion >= 80 Entonces
				nota = "B"
			sino si calificacion >= 70 Entonces
					nota = "C"
				sino si calificacion >= 60 Entonces
						nota = "D"
					sino nota = "E"
					FinSi
				FinSi
			FinSi
	FinSi
	
	Escribir "Su nota es: " + nota
FinAlgoritmo
