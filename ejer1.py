def busquedaProfunda(graph, nodo, visitado, costo, sumaCosto):
	"""
 	Función que realiza la busqueda a Profundidad por todos los nodos del grafo
   	Parámetros
	_____________
 	graph: grafo con todos los nodos conectados entre sí
 	nodo: diccionario que contiene el costo de cada conexion entre los nodos del grafo
    visitado: 
	costo:
    sumaCosto:
  	Retorno
   	____________
	sumaCosto = Variable que contiene la suma del costo de todos los nodos en el grafo
  	"""
	#marcamos el nodo actual como true
	visitado[nodo] = True
	#bucle for que recorre todos los nodos del grafo
	for vecino in graph[nodo]:
		#Verificamos si el vecino del nodo ya ha sido visitado
		if not visitado[vecino]:
			#seguimos acumulando el costo que tiene dicho nodo
			sumaCosto += costo[(nodo, vecino)]
			#llamamos de nuevo a la función busquedaProfunda
			busquedaProfunda(graph, vecino, visitado, costo, sumaCosto)

def sum_costs(graph, cost):
	"""
 	Función que obtiene el valor del costo total de todos los nodos del grafo
   	Parámetros
	_____________
 	graph: grafo con todos los nodos conectados entre sí
 	cost: diccionario que contiene el costo de cada conexion entre los nodos del grafo
  	Retorno
   	____________
	sumaCosto = Variable que contiene la suma del costo de todos los nodos en el grafo
  	"""
	 #inicializamos la lista "visitado" con un valor booleano "False" para cada uno de los elementos de la lista
	visitado = [False] * len(graph)
	#variable que contiene la suma del costo de todos los nodos del grafo y lo inicializamos en 0
	sumaCosto = 0
	#llamamos a la funcion busquedaProfunda para recorrer todos los nodos del grafo
	busquedaProfunda(graph, 0, visitado, cost, sumaCosto)
	#retornamos la suma
	return sumaCosto

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
	graph, cost = [[] for i in range(5)], {}
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	print(graph, cost)
	# añadir los nodos
	#0 a 1
	graph[0].append(1)
	graph[1].append(0)
	#0 a 2
	graph[0].append(2)
	graph[2].append(0)
	#0 a 3
	graph[0].append(3)
	graph[3].append(0)
	#1 a 3
	graph[1].append(3)
	graph[3].append(1)
	#1 a 4
	graph[1].append(4)
	graph[4].append(1)
	#4 a 2
	graph[4].append(2)
	graph[2].append(4)
	# añadiendo el costo a los nodos, todos con el valor de 2
	cost[(0, 1)] = cost[(1, 0)] = cost[(0, 2)] = cost[(2, 0)] = cost[(
	 0, 3)] = cost[(3, 0)] = cost[(1, 3)] = cost[(3, 1)] = cost[(1, 4)] = cost[(
	  4, 1)] = cost[(4, 2)] = cost[(2, 4)] = 2
	#Imprimimos el nodo y el grafo en modo de lista de listas y en un diccionario para los costos
	print(graph, cost)
	#retornamos el grafo y el costo
	return graph, cost


if __name__ == "__main__":
	grafo, costo = creacionGrafo()
	costo_total = sum_costs(grafo, costo)
	print("El costo total del grafo es:", costo_total)