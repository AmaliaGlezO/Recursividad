# Estrucura básoca de una función recursiva
#1 - Caso base: La condición que detiene el proceso
#2 - Caso recursivo: La llamada a sí misma para resolver un problema

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

lista = [2,6,7,4,8,6]
print(lista[1:])

def suma_lista(lista=[]):
    if not lista:
        return 0
    else:
        return lista[0] + suma_lista(lista[1:])
    
print(suma_lista([3,6,5,4,7,8,3,2,5,4]))
