# Pensamiento recursivo del proble ma del factorial
# def de factorial: n! = n*(n-1)*(n-1-1)*...*1

# Paso 1: Caso base. detectar donde parará el programa recursivo, condición de parada y sería a la vez el caso más fácil o conveniente
    # en este caso el factorial más fácil sería el de 0 o 1 que es 1

# Ahora se podrá encotrar una forma o patrón que facilite el código a achicarse hasta el caso base?

# Paso 2: Hacer el problema más chiquito bajo el pensamiento recursivo(que se llame a si mismo)
    # El factorial de n es igual n*(n-1)! esto debe tender al caso base
    # Acabamos de dar con una forma fácil, se va allamar a si mismo cada vez más pequeño

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * (factorial(n-1))

print(factorial(4))
    