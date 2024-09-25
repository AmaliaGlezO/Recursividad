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


# Intentemos ahora hacer una función que sume todos los elementos hasta n de la sucesión de fibonacci
# Paso 1: Caso base
    # si n=1. fibonacci_suma es 0
    # si n=2. fibonacci_suma es 1
# Paso 2: Divide y vencerás
    # si n=3. fibonacci_suma es 0+1+1 = 3
        # ya vimos el patrón. fibonacci_suma de 3 es fibonacci(3)+fibonacci(2)+fibonacci(1)
    # si n = 4. fibonacci_suma es 0+1+1+2 = 4
        # fibonacci(4)+ fibonacci(3)+fibonacci(2)+fibonacci(1)
        # fibonacci(n) + fibonacci_suma(n-1)

# bamos a descubrir si desde una función se puede llamar otra

def fibonacci_suma(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n) + fibonacci_suma(n-1)
    
print(fibonacci_suma(6))