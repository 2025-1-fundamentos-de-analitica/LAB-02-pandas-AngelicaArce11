"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    # Cargamos el archivo, indicamos que tiene encabezado y que  \t es el separador
    table = pd.read_csv(
        "files/input/tbl1.tsv",
        header=0,
        delimiter="\t",
        index_col=None
        )
    
    # Primero obtenemos solo los valores de la columna c4, con unique obtenemos un numpy con los valores sin repetir, mapeamos para que quede en mayus
    values = list(map(lambda v: v.upper(), table['c4'].unique()))
    # Ordenamos alfabeticamente
    values.sort()
    
    return values