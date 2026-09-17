#crear lista vacia
lista_nombres =[]

while True:
    variable_nombre = input("Ingrese su nombre: ")

    if variable_nombre != "salilr":
        lista_nombres.append(variable_nombre)

    if variable_nombre == "salir":
        print("Nombres Guardados: ")
        print(lista_nombres)
        break #finaliza el ciclo, solo con while en el codigo


nombre = input("Ingrese su nombre: ")
print(f"Nombre en Mayusculas {nombre.upper()}")#mayusculas
print(f"Ingrese en Minusculas {nombre.lower()}")#minusculas

if nombre.lower()== "dax":
    print("Hola Dax")
else:
    print("Tu no eres dax")  
          


#es para hacer listados hacia abajo

lista_perros = []
lista_gatos = []

while True:
    try:
        pregunta = int(input(""" 
        seleccion opcion:
        1: Registrar perros
        2: Registrar gatos
        3: Mostarar Listado de perros
        4: Mostrar Listado de gatos
        5: Salir
        """))
        #validar que opcion acepta el usuario
        if pregunta == 1:
            perro=input("Cuál es el nombre del perro: ")
            lista_perros.append(perro)

        elif pregunta ==2:
            gato=input("Cuál es el nombre del gato: ")
            lista_gatos.append(gato) 

        elif pregunta ==3:
            print("Listado de perritos")
            print(lista_perros)    

        elif pregunta ==4:
            print("Listado de gatitos")
            print(lista_gatos)

        elif pregunta ==5:
            print("Salir del sistema") 
            break   

        else:
            print("Opcion invalida")          


    except ValueError:
        print("Ingrese una opcion válida")    



