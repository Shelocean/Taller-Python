print("Ejercicio 1: Sumar dos números")
print("*"*20)

numero1 = float(input("por favor ingrese el primer número: "))
numero2 = float(input("por favor ingrese el segundo número: "))
#se calcula la suma

print(f"Resultado: {numero1 + numero2}")


print("Ejercicio 2: Área de un rectangulo")
print("*"*20)

base = float(input("por favor ingrese la base del rectangulo: "))
altura = float(input("por favor ingrese la altura del rectangulo: "))
#se calcula el área #formula:base x altura

area = base * altura

print(f"Resultado: {base * altura}")

print(f"El area del rectangulo es: {area}")


print("Ejercicio 3: Minutos a horas y minutos")
print("*"*20)

minutos_totales = int(input("Por favor ingrese la cantidad de minutos: "))

horas = minutos_totales // 60 # division -entera horas completa
minutos = minutos_totales % 60 # módulo - minutos restantes

print(f"{minutos_totales} minutos equivalen a {horas} horas y {minutos} minutos")


print("Ejercicio 4: Precio con descuento")
print("*"*20)

precio = float(input("Por favor ingrese el precio del producto:"))
descuento = float(input("Por favor ingrese el porcentaje de descuento: "))

valor_descuento = precio * (descuento / 180) # valor que se descuenta
precio_final = precio - valor_descuento # precio con descuento

print(f"El precio final a pagar es: {precio_final}")


print("Ejercicio 5: Intercambio de valores")
print("*"*20)

a = float(input("Por favor ingrese el valor de a: "))
b = float(input("Por favor ingrese el valor de b: "))

auxiliar = a # guardar temporalmente el valor de a
a = b        # a toma el valor de b
b = auxiliar # b toma el valor original de a

print(f"Después del intercambio: a = {a} , b = {b}")


print("Ejercicio 1.1:")
print("*"*20)



#Taller 1
print("Taller: Punto 1")

base = float(input("Ingrese el largo del terreno en metros: "))
altura = float(input("Ingrese el ancho del terreno en metros: "))
print(f"El perimetro del rectangulo es: {(base*2) + (altura*2)}")



print("Taller: Punto 2")


numero1 = float(input("ingrese el número 1: "))
numero2 = float(input("ingrese el número 2: "))
numero3 = float(input("ingrese el número 3: "))

print(f"El promedio de los numeros es: {(numero1 + numero2 + numero3) /3}")



print("Taller: Punto 3")

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))

print(f"""
      Hola,mi nombre es {nombre} y tengo {edad} años.""")




print("Taller: Punto 4")


pesos_cop = float(input("ingrese los pesos cop a convertir a dolar, porfa: "))
dolar = pesos_cop / 4000

print(f"Los pesos cop a dolar son: {pesos_cop} COP = {dolar} USD")



print("Taller: Punto 5")


segundos_totales = float(input("ingrese los segundos: ")) #variable

print(f"tiempo en minutos: {segundos_totales /60}")
print(f"tiempo en horas: {segundos_totales /3600}")
