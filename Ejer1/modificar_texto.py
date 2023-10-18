import sys

# Verificar si se proporcionaron los parámetros correctos
if len(sys.argv) != 3:
    print("No hay suficientes parámetros de entrada")
    sys.exit(1)

letra_cif = sys.argv[1]
letra_descif = sys.argv[2]

# Leer el contenido actual del archivo de texto
with open('resultado.txt', 'r') as prueba:
    texto = prueba.read()

# Realizar el reemplazo de la letra
texto_descifrado = texto.replace(letra_cif, letra_descif)

# Escribir el texto modificado de nuevo en el archivo
with open('resultado.txt', 'w') as resultado:
    resultado.write(texto_descifrado)

print(f'Se ha cambiado la letra "{letra_cif}" por "{letra_descif}" en el archivo "resultado.txt".')
