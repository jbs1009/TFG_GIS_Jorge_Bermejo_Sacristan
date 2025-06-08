import subprocess
import os
import sys


def archivo2lista(archivo): 
    """
    Crea una lista a partir de un archivo .txt de wgets proporcionado.

    Args
    ---------
    archivo: ruta del archivo con las línea correspondiente al comando de wget para la descarga de datos proporcionado en ENA Browser.

    Return
    ---------
    lineas: list con las líneas de los comandos para descargar las secuencias.
    """
    with open(archivo, 'r', encoding='utf-8') as file: 

        lineas = file.readlines()
        lineas = [linea.strip('\n') for linea in lineas] 

        return lineas
def prepara_subprocess(lista):
    """
    Función que prepara los comandos presentes en la lista de comandos creada por archivo2lista(), de modo que cada argumento
    del comando aparezca separados por comas, permitiendo así su posterior utilización con subprocess.

    Args
    ---------
    lista: list obtenida a partir de archivo2lista() con los comandos de wget con sus argumentos separados por espacios.

    Return
    ---------
    lista_split: list con cada uno de los comandos anteriores con los argumentos separados por comas para pasar a subprocess.
    """

    lista_split = []

    for linea in lista:
        lista_split.append(linea.split(" "))

    return lista_split
def descargar_secuencias(archivo):
    """
    Función que recibe un archivo .txt con comandos de descarga de wget obtenido de ENA Browser y ejecuta subprocess para descargar las secuencias.

    Args
    ---------
    archivo: archivo .txt con los comandos de wget para la descarga de secuencias proporcionado por ENA Browser

    Return
    ---------
    None
    """
    #Aplica archivo2lista() con el txt proporcionado
    lista_wgets = archivo2lista(archivo)
    #Aplica prepara_subprocess() con la lista de comandos
    procesos = prepara_subprocess(lista_wgets)

    for seq in procesos:
        #Ejecuta subprocess para cada secuencia
        subprocess.run(seq)
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} .txt_de_wgets")
        sys.exit()

    descargar_secuencias(sys.argv[1])