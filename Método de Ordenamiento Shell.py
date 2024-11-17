
# El Método de ordenamiento Shell es una mejora del Método de Ordenamiento por inserción ya que 
# el Método de inserción es eficiente si la lista está casi ordenada, 
# para ello el Método Shell compara elementos separados por un espacio de varias posiciones, 
# esto permite que un elemento haga “pasos más grandes” hacia su posición esperada, 
# el mismo finaliza con un Ordenamiento por inserción simple. 


from random import sample 
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100)) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample 
#(8 elementos aleatorios de la lista base)
vectorshell = sample(lista,8)

def shellsort(vectorshell):
    
    """Esta función ordenara el vector que le pases como argumento 
    con el Método Shell Sort"""
    
    print("El vector a ordenar con shell es:", vectorshell)
    
    largo = 0
    
    for i in vectorshell:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshell[i]
            j = i
            while j >= distancia and vectorshell[j - distancia] > val:
                vectorshell[j] = vectorshell[j - distancia]
                j -= distancia
            vectorshell[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    print("El vector ordenado con shell es: ", vectorshell)
    
shellsort(vectorshell)
    