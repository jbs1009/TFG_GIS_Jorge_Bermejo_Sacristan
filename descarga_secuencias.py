import subprocess
import os
import sys


def archivo2lista(archivo): 

    with open(archivo, 'r', encoding='utf-8') as file: 

        lineas = file.readlines()
        lineas = [linea.strip('\n') for linea in lineas] 

        return lineas
def prepara_subprocess(lista):

    lista_split = []

    for linea in lista:
        lista_split.append(linea.split(" "))

    return lista_split
def descargar_secuencias(archivo, destino):

    lista_wgets = archivo2lista(archivo)
    procesos = prepara_subprocess(lista_wgets)

    for seq in procesos:
        subprocess.run(seq)
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} .txt de wgets ruta destino")
        sys.exit()

    descargar_secuencias(sys.argv[1], sys.argv[2])