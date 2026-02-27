Algoritmo sin_titulo
	i = 0
	j = 0
	
	cantidad_hombres = 0
	cantidad_mujeres = 0
	
	Escribir "Cuantos datos desea ingresar?" 
	leer j
	
	Mientras i < j Hacer
		Escribir "Ingrese el género"
		leer genero
		
		Segun genero Hacer
			"hombre":
				cantidad_hombres = cantidad_hombres + 1
				i = i + 1
			"mujer":
				cantidad_mujeres = cantidad_mujeres + 1
				i = i + 1
			De Otro Modo:
				Escribir "Ingrese una opción correcta"
		Fin Segun
	FinMientras
	
	Escribir (cantidad_hombres / j) * 100, "% ", (cantidad_mujeres / j) * 100 ,"%"
FinAlgoritmo
