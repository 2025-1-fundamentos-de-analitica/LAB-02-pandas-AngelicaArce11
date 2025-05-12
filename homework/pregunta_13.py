"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    # Cargamos el archivo, indicamos que tiene encabezado y que  \t es el separador
    table1 = pd.read_csv(
        "files/input/tbl0.tsv",
        header=0,
        delimiter="\t",
        index_col=None
        )
    
    # Cargamos el archivo, indicamos que tiene encabezado y que  \t es el separador
    table2 = pd.read_csv(
        "files/input/tbl2.tsv",
        header=0,
        delimiter="\t",
        index_col=None
        )
    
    # Hacemos un join por el atributo de la clave c0
    tableResult = pd.merge(table1, table2, on='c0')

    # Agrupamos por letra (c1), ubicamos la columna que nos interesa y sumamos los valores
    return tableResult.groupby('c1')['c5b'].sum()