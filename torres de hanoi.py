def solve_hanoi(n, origen, auxiliar, destino):
    if n == 1:
        print(f"Mover disco 1 de {origen} a {destino}")
    else:
        solve_hanoi(n - 1, origen, destino, auxiliar)  # Mover n-1 discos de origen a auxiliar
        print(f"Mover disco {n} de {origen} a {destino}")  # Mover el disco n de origen a destino
        solve_hanoi(n - 1, auxiliar, origen, destino)  # Mover n-1 discos de auxiliar a destino

# Llamada a la función
n = 5  # Número de discos
solve_hanoi(n, 'Origen', 'Auxiliar', 'Destino')