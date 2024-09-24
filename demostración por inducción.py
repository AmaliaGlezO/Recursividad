# Demuestre por inducción que la función Q(n) = 1**2+2**2+...+n**2 puede expresarse como Q(n)= n(n+1)(2n+1)/6
def miembro_izquierdo(n):
    if n == 1:
        return 1
    else:
        return n**2 + miembro_izquierdo(n-1)

def miembro_derecho(n):
    q_n = (n*(n+1)*((2*n)+1))//6
    print(q_n)
    
n = 5

if miembro_izquierdo(n) == miembro_derecho(n):
    print("Queda demostrado")
else:
    print("no se cumple la igualdad")

print(f"El miembro izquierdo da {miembro_izquierdo(n)}")
print(f"El miembro derecho da {miembro_derecho(n)}")