import sys

def suma_CIGAR(cadena):
    cadena_nueva = []
    for i in cadena:
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
    with open(archivo_sam, "r") as archivo_sam, open(archivo_sam_corregido, "w") as archivo_sam_corregido:

        for linea in archivo_sam:
            
            if linea[0] == "@":
                archivo_sam_corregido.write(linea)
            
            else:
                lista_linea = linea.split("\t")
                
                if suma_CIGAR(lista_linea[5]) == len(lista_linea[9]):
                    archivo_sam_corregido.write(linea)
                


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} sam_original sam_corregido")
        sys.exit()
    
    corrige_sam(sys.argv[1], sys.argv[2])