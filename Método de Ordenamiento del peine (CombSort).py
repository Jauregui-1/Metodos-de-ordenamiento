
# El Método de ordenamiento del peine es una mejora del Método de ordenamiento de la burbuja, 
# ya que en el Método de la burbuja siempre se comparan valores consecutivos, entonces todos los 
# cambios se realizan uno por uno. 
# El Método del peine (CombSort) mejora al BubbleSort usando un espacio de tamaño superior a 1. 
# El espacio comienza con un valor grande y se reduce en un factor x en cada iteración hasta que 
# alcanza el valor 1. Por lo tanto este elimina más de una inversión con un intercambio y funciona 
# mejor que el Método de la burbuja.


from random import sample 
# Importamos un Método de la biblioteca random para generar listas aleatorias

lista = list(range(100)) # Creamos la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample 
#(8 elementos aleatorios de la lista base)
vectorcomb = sample(lista,8)
def combsort(vectorcomb):
    """Esta función ordenara el vector que le pases como argumento
    con el Método de Comb Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con comb es:",vectorcomb)
    
    largo = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorcomb:
        largo += 1
    
    
    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo
    
    # Establecemos la variable que define si es necesario o no
    #  intercambiar los numeros que se están comparando
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        # La diferencia minima es 1
        # En cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            # Ubicamos el número que está a la distancia x de i
            if vectorcomb[i] > vectorcomb[j]:
                vectorcomb[i], vectorcomb[j] = vectorcomb[j], vectorcomb[i]
                # Hacemos el intercambio de los numeros
                cambiar = True
    
    print("El vector ordenado con comb es: ",vectorcomb)

combsort(vectorcomb)