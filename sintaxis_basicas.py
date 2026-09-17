nombre ="Michel" #variable de texto (string)
documento =123 #variable numerica
direccion = "crr 46 Medellin" 
tiene_deudas = True # variable booleana

print(nombre)



print("CONCATENACIÓN USANDO +")
print("=" * 30)

print("Mi nombre es: " + nombre)
print("Mi numero de documento es : " + str(documento))

print("nombre es: " + nombre + " documento es: " + str(documento))



print("\nCONCATENACIÓN USANDO ,")
print("=" * 30)

print("Mi nombre es:", nombre, "y mi documento es:", documento)


print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

print(f"Mi nombre es: {nombre} y mi documento es: {documento}")


print("\nMOSTRAR VARIAS VARIABLES CON F-STRINGS")
print("=" * 30)

print(f"""
nombre:         {nombre}
documento:      {documento}
direccion:      {direccion}
¿tiene deudas?: {tiene_deudas}
""")

print("=" * 30)

print(f"""
nombre:{nombre}
documento:{documento}
direccion:{direccion}
¿tiene deudas?:{tiene_deudas}
""")

print(f"\n Hola, {nombre}!")

print(f"Bienvenida {nombre} a python.\n")

print("\n moon")