import sys

def suma_CIGAR(cadena):
    """
    Calcula la suma resultante de la cadena o puntuación CIGAR de un read en un archivo SAM.

    Args
    --------
    cadena: str, cadena CIGAR de un read en un archivo SAM

    Returns
    --------
    int, suma resultante de dicha cadena CIGAR proporcionada
    """
    cadena_nueva = []
    for i in cadena:
        #Comprueba si la posición de la cadena es un entero (lo almacena) o una letra (la almacena si requiere 
        # de una resta posterior [como una D correspondiente a una delección], sino, almacena un '.')
        try:
            int(i)
            cadena_nueva.append(i)

        except ValueError:
            if i not in ("D", "N", "H", "P"):
                cadena_nueva.append(".")
            else:
                cadena_nueva.append(i)

    cadena_nueva = ''.join(cadena_nueva)
    
    valor_resta = 0

    #Almacena en el valor_resta la suma de los números que preceden a las letras D, N, H o P. El total se restará de la suma final.
    corrige = [i for i in ("D", "N", "H", "P") if i in cadena_nueva]
    if len(corrige) != 0:
        for letra in corrige:
            posLetra = cadena_nueva.find(letra)
            valor_resta += int(cadena_nueva[posLetra - 1])
            cadena_nueva = cadena_nueva.replace(letra, ".")
    
    cadena_nueva = cadena_nueva.split('.')
    cadena_nueva = [int(i) for i in cadena_nueva if i != '']
    
    return sum(cadena_nueva) - valor_resta

def corrige_sam(archivo_sam, archivo_sam_corregido):
    """
    Función que recibe la ruta de un archivo SAM y realiza una serie de comprobaciones y correcciones necesarias para convertirlo
    a archivo BAM (correcciones tomadas como referencia de los errores que imprimía por pantalla SAMtools al convertir a BAM)

    Args
    --------
    archivo_sam: ruta del archivo SAM a corregir
    archivo_sam_corregido: ruta de destino para el archivo SAM corregido

    Returns
    --------
    None
    """
    with open(archivo_sam, "r") as archivo_sam, open(archivo_sam_corregido, "w") as archivo_sam_corregido:

        for linea in archivo_sam:
            
            if linea[0] == "@":
                #Mantiene toda la parte del header del archivo SAM original, comenzando sus líneas por @.
                archivo_sam_corregido.write(linea)
            
            else:

                if linea.count("SRR") > 1:
                    #Comprueba si hay más de un read por línea en el archivo SAM y los separa en líneas diferentes en caso afirmativo
                    indice = linea[3:].find("SRR") + 3
                    
                    linea1 = linea[:indice]
                    lista_linea1 = linea1.split("\t")
                    
                    linea2 = linea[indice:]
                    lista_linea2 = linea2.split("\t")
                    
                    #Comprueba si las líneas tienen la cantidad de campos esperada
                    if len(lista_linea1) >= 10:
                        
                        #Comprueba si la suma de la cadena del campo CIGAR coincide con la longitud del read para añadir la línea al SAM corregido
                        if suma_CIGAR(lista_linea1[5]) == len(lista_linea1[9]):
                            archivo_sam_corregido.write(linea1 + "\n")

                    if len(lista_linea2) >= 10:
                        #Mismas comprobaciones para la segunda línea separada

                        if suma_CIGAR(lista_linea2[5]) == len(lista_linea2[9]):
                            archivo_sam_corregido.write(linea2)
                    
                else:
                    lista_linea = linea.split("\t")

                    if len(lista_linea) >= 10:
                    
                        if suma_CIGAR(lista_linea[5]) == len(lista_linea[9]):
                            archivo_sam_corregido.write(linea)
                


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} sam_original sam_corregido")
        sys.exit()
    
    corrige_sam(sys.argv[1], sys.argv[2])