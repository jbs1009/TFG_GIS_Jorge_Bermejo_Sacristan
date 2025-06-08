# TFG_GIS_Jorge_Bermejo_Sacristan
# «Proyecto de investigación bioinformática para la identificación de variantes genéticas relacionadas con la Enfermedad de Parkinson»

## Resumen
La enfermedad de Parkinson es la segunda enfermedad neurodegenerativa más común del sistema nervioso central (SNC), así como el desorden del movimiento más frecuente. En este Trabajo de Fin de Grado se ha desarrollado un proyecto de investigación completo con la finalidad de explorar variantes de expresión génica que puedan presentar una relación con esta enfermedad, a partir de datos de secuenciación masiva de RNA-Seq. Dicho proyecto ha constado de un análisis secundario de estos datos, alineándolos respecto a la versión hg38 del genoma humano, para identificar con qué regiones se correspondían las lecturas iniciales manejadas, y un análisis terciario destinado a realizar un estudio de expresión diferencial, a partir del cual se han seleccionado una serie de genes que presentan una distinta expresión en pacientes con y sin Parkinson, la cual se pudo ver amortiguada tras aplicar sobre el paciente un tratamiento de estimulación cerebral profunda (DBS). Finalmente, de entre los genes de interés localizados, se ha caracterizado una variación morfológica y estructural del receptor acoplado a proteína G, codificado por el gen ADORA2A, donde, al realizar su predicción estructural con AlphaFold2, se observa un acortamiento de su extremo C-terminal, dificultando o imposibilitando su correcta unión a la célula, lo que podría estar relacionado con la enfermedad de Parkinson.

## Abstract
Parkinson's disease is the second most common neurodegenerative disease of the central nervous system (CNS), as well as the most common movement disorder. This thesis developed a comprehensive research project to explore gene expression variants that may be related to this disease, using massive RNA-Seq sequencing data. This project consisted of a secondary analysis of these data, aligning them with the hg38 version of the human genome to identify which regions the initial reads corresponded to, and a tertiary analysis aimed at conducting a differential expression study. From this, a series of genes were selected that exhibit different expression in patients with and without Parkinson's disease, which expression was attenuated after the patient underwent deep brain stimulation (DBS). Finally, among the genes of interest located, a morphological and structural variation of the G protein-coupled receptor, encoded by the ADORA2A gene, has been characterized, where, when performing its structural prediction with AlphaFold2, a shortening of its C-terminal end is observed, making its correct binding to the cell difficult or impossible, which could be related to Parkinson's disease.

## WORKFLOW SEGUIDO
![workflow](https://github.com/user-attachments/assets/0e6051c7-5fb6-45ca-bc3c-8b4b9d807a1f)

## VISUALIZACIÓN DE RESULTADOS FINALES
El receptor de proteína G codificado por ADORA2A original, sin la variación identificada, presenta la siguiente estructura:
![proteina_original](https://github.com/user-attachments/assets/28a558a4-b928-4213-bb1f-9fe017e56dae)

Sin embargo, con la variante de expresión identificada, vemos que la proteína mutada codificada presenta su C-terminal bastante acortado respecto a la original, lo cual le hace perder puntos de unión y funcionalidad:
![proteina_mutada](https://github.com/user-attachments/assets/4e113da5-c468-4abb-b349-1d654d25e6e1)

Se puede observar el alineamiento de estas dos estructuras tridimensionales en las siguientes imágenes desde diferentes ángulos (proteína verde original, proteína roja mutada):
![pymol1](https://github.com/user-attachments/assets/dd6f2368-874f-4a9e-816c-9540f51a7816)
![pymol2](https://github.com/user-attachments/assets/eeebec72-a60c-4d72-b7fb-cb3c61c67262)
![pymol3](https://github.com/user-attachments/assets/d042b894-a26f-44da-a449-eeaa460ff692)



