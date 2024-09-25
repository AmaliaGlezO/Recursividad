# Crea una función recursiva que encuentre el n-esimo número de fibonacci

# Análisis inicial:
# Secuencia de Fibonacci: 0,1,1,2,3,5,8,13,...

# Paso 1: Caso base. sería que me pidan cual es el número 1 de su secuencia
    # Si n = 1. 1 en la sucesión de fibonacci es 0
    # o n = 2. 2 en la sucesi´´on en 1

# Paso 2: Dibide y vencerás.
    # Qué pasaría si n es 3. sería 1. el resultado de 0+1
    # Qué pasaría si n es 4. sería 2. el resultado de 1+1
    # Encontramos un patrón recursivo. Porque fibonacci de n es la suma de fibonacci de n-1 y n-2
    # Además tenemos quien es fibonacci en 1 y 2

# ESTAMOS LISTOS

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(6))
