nombre = "Amalia"
edad = 20
altura = 1.60
nota = 92

# CONDICIONALES
if nota >= 90:
    print("Sobresaliente")
elif nota >= 75:
    print("Bien")
elif nota >= 60: 
    print("Suficiente")
else:
    print("Insuficiente")
# Acabamos de ver que el if no le importa ser llamado. El trabaja porque está aquí me toca y paso

# BUCLES
notas = [['Amalia','juan','luis','Yandri','Ana'],[92,34,76,68,100]]

for nota in notas[1]:
    if nota >= 90:
        print(notas[0][0],"Sobresaliente")
    elif nota >= 75:
        print(notas[0][1],"Bien")
    elif nota >= 60: 
        print(notas[0][2],"Suficiente")
    else:
        print(notas[0][3],"Insuficiente")

# Aquí podemos ver que tanto el if como el for me arranca sin yo llamarlo, ahora cuando estoy haciendo un programa yo quiero que eso funcione cuando yo quiera, lo puedo meter dentro de un def
# FUNCIONES
def sacar_promedio(nombre,calificaciones = []):
    promedio = sum(calificaciones)/len(calificaciones)
    print(f"El promedio de {nombre} es de {promedio} puntos")

sacar_promedio("Amalia",[97,78,86,90,100])