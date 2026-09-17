
#Repaso clase pasada
"""
#Solicitar nombre al usuario
var_nombre = input("Por favor ingrese su nombre: ")

#Solicitar edad al usuario
var_edad = int(input(f"{var_nombre} Por favor ingrese su edad: "))

#Condicion validar si es edad > 18
if var_edad >= 18:
    print(f"{var_nombre} usted es mayor de edad.")
else:
    print(f"{var_nombre} Usted es menor de edad.")

"""#bloqueado o comentado



# Ejercicio 1: Determinar si un número es positivo, negativo o cero
numero = float(input("Ingrese un número: ")) #int / float Conversión de texto a número entero o decimal


if numero > 0: #Ejecuta un bloque solo si la condición es verdadera
    print(f"El número {numero} es positivo")

elif numero < 0: #Evalúa una segunda condición si la anterior fue falsa
    print(f"El número {numero} es negativo")

else: #Se ejecuta cuando ninguna condición anterior se cumplió
    print(f"El número {numero} es cero")


# Ejercicio 2: Verificar si una persona es mayor de edad
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad.")
else: 
    print("Es menos de edad.")


#Ejercicio 3: determinar si un número es par o impar
numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0: # si el residuo es 0 → es par # == igualdad exacta
   print(f"{numero} es par") 
else:
    print(f"{numero} es impar")



# Ejercicio 4: Clasificar una nota académica
nota = float(input("Ingrese la nota obtenida (0.0 a 5.0): "))

if  nota >= 5.0:
    print("Nota invalida")
elif nota >= 4.5:
    print("Desempeño superior")
elif nota >= 3.5:
    print("Desempeño alto")
elif nota >= 3.0:
    print("Desempeño básico")
elif nota < 0.0:
    print("Nota invalida")
else:
    print("Desempeño bajo")



# Ejercicio 5: Determinar el mayor de tres números
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))

if n1 >= n2 and n1 >= n3:
  mayor = n1
elif n2 >= n1 and n2 >= n3:
  mayor = n2
else:
    mayor = n3

print(f"El mayor de los tres números es: {mayor}")




#Taller 2: solicitar nombre y edad al usuario, si es mayor de edad mostrar un mensaje de bienvenida, si es menor de edad mostrar un mensaje de despedida


#ejercicio 1
nombre =input("Ingrese su nombre: ")
edad =int(input("Ingrese su edad: "))

if edad <0:
    print(f"Error: la edad {edad} no es válida. Por favor ingrese un numero positivo.")
elif edad >=18 :
    print(f"Bienvenido {nombre}, tienes {edad} años, eres mayor de edad.")
else:
    print(f"Lo sentimos {nombre}, aun te faltan {18- edad} años para ser mayor de edad.")



#ejercicio 2
nombre = input("Ingrese su nombre:")
nota =float(input("Ingrese la nota obtenida: "))


if nota <0.0 or nota >5.0: 
    print("Error la nota no es válida.")
elif nota > 4.5 and nota <= 5.0:
    print(f"Apreciado {nombre}, su nota final es {nota}, su desempeño fue Excelente, has sido aprodado.")
elif nota >=3.5 and nota <=4.4:
    print(f"Apreciado {nombre}, su nota final es {nota}, su desempeño fue Bueno, has sido aprobado.")
elif nota >=3.0 and nota <=3.4:
    print(f"Apreciado {nombre}, su nota final es {nota}, su desempeño fue Aceptable, has sido aprobado.")
elif nota >=0 and nota <=2.9:
    print(f"Apreciado {nombre}, su nota final es {nota}, su desempeño fue Insuficiente, has sido reprobado.")
else:  
    print("")

    
#ejercicio 3_cliente y valor
nombre = input("ingrese su nombre: ")
valor_compra =float(input(f"{nombre} ingrese el valor de la compra: ")) 
  
if valor_compra <0:
    print(f"{nombre} el valor de la compra es invalido")  
elif valor_compra <100000:
    print(f"{nombre}el valor de la compra es {valor_compra} y no tiene descuento")

elif valor_compra >=100000 and valor_compra <299999:
    descuento = valor_compra * 0.10
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 10% {descuento} y el total a pagar es {total}")
    
elif valor_compra >=300000 and valor_compra <499999:
    descuento = valor_compra * 0.15
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 15% {descuento} y el total a pagar es {total}")

elif valor_compra >=500000 and valor_compra <999999:
    descuento = valor_compra * 0.20
    total = valor_compra - descuento
    print(f"{nombre} el valor de la compra es {valor_compra} y el descuento es 20% {descuento} y el total a pagar es {total}")



#ejercicio 4
nombre_ciudad = input("Ingrese nombre de la ciudad: ")
Temperatura = float(input("La temperatura en grados celsius (10° a 32°:)"))

if Temperatura >= 32:
    print("Muy caliente")
elif Temperatura >= 26:
    print("Caliente")
elif Temperatura >= 18:
    print("Templado")
elif Temperatura >= 10:
    print("Fria")
elif Temperatura <= 10:
    print("Muy fria")

if Temperatura <18:
    print(f"Temperatura baja: llevar abrigo")



# Ejercicio 5: empleado y salario

var_nombre = input("Ingrese nombre del empleado: ")
horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
valor_hora = float(input("Ingrese el valor por hora: "))

salario = valor_hora * horas_trabajadas
var_seguridad = salario * 0.08 


if horas_trabajadas < 0 or valor_hora < 0:
    print("Error: Las horas trabajadas y el valor por hora deben ser números positivos.")

elif horas_trabajadas <= 160:

    salario_neto = salario - var_seguridad
    print(f""" === RESUMEN DE PAGO SALARIO ===
    -Salario: {salario} 
    -Seguridad social {var_seguridad} 
    -Salario neto es: {salario_neto}
    """)

elif horas_trabajadas > 160:

    horas_extras = horas_trabajadas - 160
    valor_horas_extras= (horas_extras* valor_hora )* 1.25
    salario_neto = (valor_hora * horas_trabajadas) + valor_horas_extras - var_seguridad

    print (f""" == RESUMEN DE PAGO SALARIO ==
    -Horas extras {horas_extras} Valor Horas Extras {valor_horas_extras}
    -Salario basico: {salario}
    -seguridad social {var_seguridad} 
    -salario total {salario_neto} 

""")
