import sys

def arregla_qual(calidad):
    return calidad[1:]

def corrige_csfastq(archivo_csfastq, archivo_csfastq_corregido):

    with open(archivo_csfastq, "r") as archivo_csfastq, open(archivo_csfastq_corregido, "w") as archivo_csfastq_corregido:

        while True:

            identificador = archivo_csfastq.readline().strip()

            if not identificador:
                break

            secuencia = archivo_csfastq.readline().strip()
            separador = archivo_csfastq.readline().strip()
            calidad = archivo_csfastq.readline().strip()

            calidad_corregida = arregla_qual(calidad)

            archivo_csfastq_corregido.write(f"{identificador}\n{secuencia}\n{separador}\n{calidad_corregida}\n")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} csfastq_original csfastq_corregido")
        sys.exit()
    
    corrige_csfastq(sys.argv[1], sys.argv[2])