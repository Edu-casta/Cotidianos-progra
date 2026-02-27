Algoritmo cuarto_ejercicio
	Escribir "Cuantos números desea ingresar: "
	leer cantidad_numeros
	nums = 0
	
	Mientras cantidad_numeros > 0 Hacer
		Limpiar Pantalla
		Escribir "Ingrese su número: "
		leer num
		
		nums = nums + num 
		cantidad_numeros = cantidad_numeros - 1
	Fin Mientras
	
	Escribir nums
FinAlgoritmo
