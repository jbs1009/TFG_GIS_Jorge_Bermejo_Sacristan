import subprocess
import os
import sys


def lista_seqs(directorio):

    lista = os.listdir(directorio)

    return lista
def asigna_nombre_sam(secuencia, num_prueba):

    archivo_sam = secuencia + '_prueba' + str(num_prueba) + '.sam'

    return archivo_sam
def alinea_HISAT2(directorio, num_prueba):

    lista_secuencias = lista_seqs(directorio)
    
    for secuencia in lista_secuencias:
        archivo_sam = asigna_nombre_sam(secuencia, num_prueba)
        subprocess.run('hisat2', '-q', '-p', '124', '-x', 'grch38/genome', '-U', secuencia, '-S', archivo_sam)
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} directorio_secuencias número de prueba")
        sys.exit()
    
    alinea_HISAT2(sys.argv[1], sys.argv[2])

