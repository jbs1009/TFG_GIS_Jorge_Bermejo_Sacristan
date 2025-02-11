def convierte_seq(secuencia):

    dicc_convers = {"T0": "T", "T1": "G", "T2": "C", "T3": "A", "T.": "N", "C0": "C", "C1": "A", "C2": "T", "C3": "G", "C.": "N", "G0": "G", "G1": "T", "G2": "A", "G3": "C", "G.": "N", "A0": "A", "A1": "C", "A2": "G", "A3": "T", "A.": "N", "N0": "N", "N1": "N", "N2": "N", "N3": "N", "N.": "N"}
    
    base_actual = secuencia[0]

    seq_fastq = [base_actual]

    for pos in secuencia[1:]:
        base = dicc_convers[str(base_actual) + str(pos)]
        seq_fastq.append(base)
        base_actual = base

    secuencia_fastq = ''.join(seq_fastq)

    return secuencia_fastq
def csfastq_a_fastq(archivo_csfastq, archivo_fastq):

    with open(archivo_csfastq, "r") as archivo_csfastq, open(archivo_fastq, "w") as archivo_fastq:

        while True:

            identificador = archivo_csfastq.readline().strip()

            if not identificador:
                break

            secuencia = archivo_csfastq.readline().strip()
            separador = archivo_csfastq.readline().strip()
            calidad = archivo_csfastq.readline().strip()

            secuencia_fastq = convierte_seq(secuencia)

            archivo_fastq.write(f"{identificador}\n{secuencia_fastq}\n{separador}\n{calidad}")