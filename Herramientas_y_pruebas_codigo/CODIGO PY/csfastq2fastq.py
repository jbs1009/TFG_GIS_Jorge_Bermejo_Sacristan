import sys

def convierte_seq(secuencia):
    """
    Función que realiza la conversión desde una secuencia proporcionada en Color-Space, a una secuencia en Base-Space (a partir
    del código creado en Perl con esta misma funcionalidad)

    Args
    ---------
    secuencia: str, cadena con las posiciones en formato Color-Space

    Returns
    ---------
    secuencia_fastq: str, cadena con las posiciones equivalentes en formato Base-Space 
    """

    #Se inicializa el diccionario de conversiones, donde se asigna a cada par "base-número_siguiente", la base que le corresponde.
    #Cuando el siguiente "número o color" a una base calculada, es ".", esta pasa a ser N, indeterminado.
    #A partir de aparecer una N, venga el número que venga después, seguirá siendo N.
    dicc_convers = {"T0": "T", "T1": "G", "T2": "C", "T3": "A", "T.": "N", "C0": "C", "C1": "A", "C2": "T", "C3": "G", "C.": "N", "G0": "G", "G1": "T", "G2": "A", "G3": "C", "G.": "N", "A0": "A", "A1": "C", "A2": "G", "A3": "T", "A.": "N", "N0": "N", "N1": "N", "N2": "N", "N3": "N", "N.": "N"}
    
    base_actual = secuencia[0]

    seq_fastq = [base_actual]

    for pos in secuencia[1:]:
        #Se consulta en el diccionario de conversiones el valor correspondiente a la clave formada por la base actual y la posicion, que será la siguiente.
        base = dicc_convers[str(base_actual) + str(pos)]
        seq_fastq.append(base)
        #base actual pasa a ser la base convertida y se repite el proceso con la siguiente posición
        base_actual = base

    secuencia_fastq = ''.join(seq_fastq)

    return secuencia_fastq
def csfastq_a_fastq(archivo_csfastq, archivo_fastq):
    """
    Función que recibe un archivo en formato CSFASTQ y convierte su secuencia a formato FASTQ convencional (basándonos en la
    conversión propuesta en el código de Perl mencionado en la Memoria y Anexos.)

    Args
    ---------
    archivo_csfastq: ruta del archivo en formato CSFASTQ, con la secuencia en Color-Space, que se desea convertir a FASTQ, secuencia en Base-Space
    archivo_fastq: ruta de destino del archivo convertido a formato FASTQ

    Returns
    ---------
    None 
    """
    with open(archivo_csfastq, "r") as archivo_csfastq, open(archivo_fastq, "w") as archivo_fastq:

        while True:

            identificador = archivo_csfastq.readline().strip()

            if not identificador:
                break

            secuencia = archivo_csfastq.readline().strip()
            separador = archivo_csfastq.readline().strip()
            calidad = archivo_csfastq.readline().strip()

            #Aplica la función convierte_seq() a la secuencia en Color-Space
            secuencia_fastq = convierte_seq(secuencia)

            archivo_fastq.write(f"{identificador}\n{secuencia_fastq}\n{separador}\n{calidad}\n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} ruta_archivo_csfastq ruta_archivo_fastq")
        sys.exit()
    
    csfastq_a_fastq(sys.argv[1], sys.argv[2])