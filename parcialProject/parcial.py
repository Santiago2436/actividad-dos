#Enteros
entero = 83
cadena = str(entero)
print(cadena)  # Salida: "83"

#Decimales
decimal = 6.70
cadena = str(decimal)
print(cadena)  # Salida: "6.70"


#Cadena
cadena = "132.34"
decimal = float(cadena)
print(decimal)  # Salida: 132.34

#Multilíneas de cadenas
texto = """
En un lugar de la Mancha,
de cuyo nombre no quiero acordarme,
no ha mucho tiempo que vivía un hidalgo.
"""

#funcion len()
cadena = "Hola, mundo"
print(len(cadena))  # Salida: 11

cadena = "Hola, mundo"

#Obtener los primeros n caracteres
n = 5
primeros_n = cadena[:n]
print(primeros_n)  # Salida: "Hola,"

#Obtener los caracteres de en medio
inicio = 3
fin = 7
medio = cadena[inicio:fin]
print(medio)  # Salida: "a, m"

#Obtener los últimos n caracteres
ultimos_n = cadena[-n:]
print(ultimos_n)  # Salida: "mundo"

#Función upper()
cadena = "Hola, mundo"
print(cadena.upper())  # Salida: "HOLA, world"

#Función lower()
print(cadena.lower())  # Salida: "hello, mundo"


#Multilineas de cadenas de caracteres
texto_multilinea = "Este es un ejemplo " \
                   "de una cadena " \
                   "multilínea en Python."
print(texto_multilinea)

#funcion strip()
cadena = "  Hello , pluton  "
print(cadena.strip())  # Salida: "Hello, pluton"

#funcion replace()
cadena = "Homer, stech"
print(cadena.replace("stech", "Python"))  # Salida: "Homer, Python"

#funcion split()
cadena = "Erick, Santiago"
print(cadena.split())  # Salida: ['Erick,', 'Santiago']

#Formato de cadenas F-String.
nombre = "Erick"
edad = 19
print(f"Me llamo {nombre} y tengo {edad} años.")  # Salida: "Me llamo Ercik y tengo 19 años."













