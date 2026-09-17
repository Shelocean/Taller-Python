"""
try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:#siempre se cierra con ese en un try
    print("Error: Por favor, ingrese un número válido.")

"""
#ciclo infinito
#for- se repite un bloque de código un número determinado de veces
#while- se repite como un bucle infinito hasta que se cumpla una condición

"""
while True:
    print("Hola Mundo")
"""    
"""
edad =18
while edad >=18:
    try:
        edad = int(input("Ingrese su edad: "))
        print(f"Su edad es: {edad}")
    except ValueError:
        print("Ingreseun número valido")

print("Menor de edad. Saliendo del sistema.")
#Si no se cumple el while.(debe estar escrito al nivel del while para que funcione) Esto es lo que mostrara cuando el ciclo finalice
"""
"""

try:
    numero = int(input("Ingrese un número entero: "))
    print(f"El número ingresado es: {numero} ")
except ValueError:
    print("Error: debe ingresar un número entero válido.")


try:
    dividiendo = float(input("Ingrese el dividendo: "))
    divisor = float(input("Ingrese el divisor:"))    
    resultado = dividiendo / divisor
    print(f"Resultado: {dividiendo} / {divisor} = {resultado}")
except  ZeroDivisionError:
    print("Error: no es posible dividir entre cero.")
except ValueError:
    print("Error: Ingrese únicamente valores numéricos.")  



try:
    edad = int(input("Ingrese su edad: "))
except ValueError:
    print("Error: la edad debe ser un número entero.")
else: #else  → se ejecuta solo si NO ocurrió ninguna excepción
    if edad >=18:
        print("Acceso permitido.")
    else: 
        print("Accseso denegado: debe ser mayor de edad.")
finally:
    print("Verificación finalizada.")#finally → se ejecuta SIEMPRE, con o sin error



while True:
    try:
        nota = float(input("Ingrese una nota entre 0.0 y 5.0: "))
        if nota <=0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.") #raise — lanzar una excepción personalizada
        break #Sale del ciclo si el valor es válido
    except ValueError as e:
        print(f"Entrada inválida: {e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")



def calcular_promedio(notas):
    if len(notas) == 0:
        raise ValueError("La lista de notas no puede estar vacía.")
    return sum(notas) / len(notas)

try:
    n = int(input("¿Cuántas notas va a ingresar? "))
    notas = []
    for i in range(n):
        nota = float(input(f" Nota {i + 1}: "))
        notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")
"""
#una variable solo guarda 1 cosa
#=a [] es una lista
