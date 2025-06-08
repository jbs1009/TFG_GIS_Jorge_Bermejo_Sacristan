import sys

def arregla_qual(calidad):
    """
    Desecha la posición inicial sobrante de la calidad de un archivo CSFASTQ.
    
    Args
    ---------
    calidad: str, cadena correspondiente a la calidad original de un archivo CSFASTQ.

    Returns
    ---------
    str, cadena excluyendo la primera posición de la calidad
    """
    return calidad[1:]

def corrige_csfastq(archivo_csfastq, archivo_csfastq_corregido):
    """
    Función que corrige un archivo en formato CSFASTQ eliminando la posición inicial sobrante de las líneas correspondientes a su calidad.

    Args
    ---------
    archivo_csfastq: ruta del archivo en formato CSFASTQ que se desea corregir, pasado como entrada
    archivo_csfastq_corregido: ruta de destino del archivo en formato CSFASTQ, una vez corregido

    Returns
    ---------
    None
    """

    with open(archivo_csfastq, "r") as archivo_csfastq, open(archivo_csfastq_corregido, "w") as archivo_csfastq_corregido:

        while True:

            identificador = archivo_csfastq.readline().strip()

            if not identificador:
                break

            secuencia = archivo_csfastq.readline().strip()
            separador = archivo_csfastq.readline().strip()
            calidad = archivo_csfastq.readline().strip()

            #Aplica la función arregla_qual() sobre la línea de calidad a corregir
            calidad_corregida = arregla_qual(calidad)

            archivo_csfastq_corregido.write(f"{identificador}\n{secuencia}\n{separador}\n{calidad_corregida}\n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} csfastq_original csfastq_corregido")
        sys.exit()
    
    corrige_csfastq(sys.argv[1], sys.argv[2])