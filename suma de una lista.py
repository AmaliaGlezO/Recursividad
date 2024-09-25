# Haga una función recursiva que sume todos los elementos de una lista

# Paso 1: Caso Base------- Que la lista tenga un solo elemento
    # En ese caso suma_lista = al elemento osea lista[0]
# Paso 2: Divide y vencerás
    # En caso de tener 2 elementos suma_lista = lista[0] + lista[1]

# Vamos a explorar propiedades de listas a ver que pasa
lista_prueba = [3,2,5,3,2,1]
n_prueba = len(lista_prueba)
print(n_prueba) 

print(lista_prueba[n_prueba-1])
print(lista_prueba[:n_prueba-1])

# Bien el len de una lista me da la cantidad exacta de elementos de la lista
# pero podemos jugar con esto
# Paso 2: Divide y vencerás
    # En caso de tener 2 elementos suma_lista = lista[0] + lista[1]
    # En caso de una lista de n elementos. suma_lista  = lista[n-1] + lista[n-2]


def suma_lista(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        return lista[n-1] + suma_lista(lista[:n-1])
    
print(suma_lista([2,3,4]))