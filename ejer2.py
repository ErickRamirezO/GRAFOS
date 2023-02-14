def suma_costos_nodos_multiples_conexiones(graph, cost):
    """
    Función que calcula la suma de los costos de los nodos que tienen más de 1 hijo o conexión.

    Parámetros
    ____________
    graph: grafo con todos los nodos conectados entre sí
    cost: diccionario que contiene el costo de cada conexión entre los nodos del grafo

    Retorno
    ____________
    total_cost: suma de los costos de los nodos que tienen más de 1 hijo o conexión
    """
	#inicializamos la variable suma a 0
    suma = 0
	#iniciamos un bucle for que itera por todo el grafo
    for node in range(len(graph)):
		# Verificamos si un nodo tiene más de una conexión
        if len(graph[node]) > 1:
			#iteramos por los hijos del nodo actual
            for connection in graph[node]:
				# Si es así, sumamos su costo
                suma += cost[(node, connection)]
	#retornamos la suma calculada
    return suma

def creacionGrafo():
	"""
 	Función que nos permite crear una lista de lista que representa a los nodos del grafo y sus conexiones
  	además de añadir el costo a cada conexion entre nodos usando un diccionario.
   	Parámetros
	_____________
 	No tiene parámetros
  	Retorno
   	____________
	graph: grafo con todos los nodos conectados entre sí
 	cost: diccionario que contiene el costo de cada conexion entre los nodos del grafo
  	"""
	# creación del grafo y diccionario de costos
	graph, cost = [[] for i in range(6)], {}
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	print(graph, cost)
	# añadir los nodos
	#0 a 2
	graph[0].append(2)
	graph[2].append(0)
	#0 a 4
	graph[0].append(4)
	graph[4].append(0)
	#0 a 5
	graph[0].append(5)
	graph[5].append(0)
	#1 a 4
	graph[1].append(4)
	graph[4].append(1)
	#1 a 3
	graph[1].append(3)
	graph[3].append(1)
	#4 a 3
	graph[4].append(3)
	graph[3].append(4)
	#2 a 3
	graph[2].append(3)
	graph[3].append(2)
	# añadiendo el costo a los nodos, todos con el valor de 1
	cost[(0, 2)] = cost[(2, 0)] = cost[(0, 4)] = cost[(4, 0)] = cost[(
	 0, 5)] = cost[(5, 0)] = cost[(1, 4)] = cost[(4, 1)] = cost[(1, 3)] = cost[(
	  3, 1)] = cost[(4, 3)] = cost[(3, 4)] = cost[(2, 3)] = cost[(3, 2)] = 1
	#retornamos el grafo y el costo
	return graph, cost


if __name__ == "__main__":
	#llamamos a la funcion creacionGrafo y asignamos a los valores de retorno correspondientes
	grafo, costo = creacionGrafo()
	#asignamos el valor que retorne de la funcion a costo_total
	costo_total = suma_costos_nodos_multiples_conexiones(grafo, costo)
	#Imprimimos la suma calculada
	print("\nLa suma de los costos de los nodos que tienen más de una conexión es: ", costo_total)