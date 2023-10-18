# Leer el contenido del archivo de texto
with open('prueba.txt', 'r') as archivo:
    texto = archivo.read()

#Crear un array para contar las veces que se repite cada letra
apariciones = {}

# Recorrer el texto y contar las apariciones de cada letra
for letra in texto:
    if letra.isalpha():
        letra = letra.lower()  # Convertir la letra a minúscula
        if letra in apariciones:
            apariciones[letra] = apariciones[letra] + 1
        else:
            apariciones[letra] = 1

apariciones_ord = sorted(apariciones)

# Imprimir las apariciones de cada letra
for letra in apariciones_ord:
    print(f'{letra}: ' + str(apariciones[letra])) 
