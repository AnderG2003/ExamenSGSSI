#!/bin/bash

# Pedir valores de parametros
echo "Introduce la carpeta en la que buscar el hash_md5 de la imagen"
read carpeta
echo "Introduce el hash_md5"
read hash_md5

# Comprobar si se proporcionaron ambos argumentos
if [ -z "$carpeta" ] || [ -z "$hash_md5" ]; then
  echo "Faltan argumentos."
  echo "Uso: $0 -d <carpeta> -h <hash_md5>"
  exit 1
fi

# Comprobar si la carpeta existe
if [ ! -d "$carpeta" ]; then
  echo "La carpeta '$carpeta' no existe."
  exit 1
fi

# Buscar el hash MD5 en todos los archivos de la carpeta
encontrado=false

for archivo in "$carpeta"/*; do
    # Calcular el hash MD5 del archivo actual
    hash_a=$(md5sum "$archivo")
    hash_archivo=$(echo $hash_a | cut -d ' ' -f 1)
    if [ "$hash_archivo" == "$hash_md5" ]; then
        echo "El hash MD5 $hash_md5 se encontró en el archivo: $archivo"
        encontrado=true
        break  # Terminar la búsqueda después de encontrar una coincidencia
    fi
done

if [ "$encontrado" == "false" ]; then
    echo "El hash MD5 $hash_md5 no se encontró en ningún archivo de la carpeta."
fi
