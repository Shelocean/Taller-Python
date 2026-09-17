#ciclo for repete cantidades

#Repetir cantidad de veces
"""
for i in range(2):# i es una variable para el for, en programacion es estandar 
    print(f"{i} Hola mundo.")
"""

#Configuar pocicion inicial y final
"""
for i in range(1, 11):
    print(f"{i} Hola mundo.")
"""
#(1pocición inicial, 2pocición final, 3incremento)
"""
for i in range(0, 101, 5):
    print(f"{i} Hello world")
"""

#adivina el numero secreto 3 intentos
import random

numero_secreto =  random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto (1-10): "))

    if numero == numero_secreto :
        print("✨Felicidades adivinaste✨.")
        break
    else: 
        intentos_restantes = intentos - (i + 1)
        print(f"❌ Te quedan {intentos_restantes} intentos.")
                           #3 - (0 + 1) =1
                           #3 - (1 + 1) =2
                           #3 - (2 + 1) =0
        if intentos_restantes == 0:
        #verificar si quedan intentos y mostrar el numero 
           print(f"El numero secreto era: {numero_secreto}")



