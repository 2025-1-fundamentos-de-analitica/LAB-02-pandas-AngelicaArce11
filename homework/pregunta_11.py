"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_11():
     """
     Construya una tabla que contenga `c0` y una lista separada por ',' de
     los valores de la columna `c4` del archivo `tbl1.tsv`.

     Rta/
          c0       c4
     0     0    b,f,g
     1     1    a,c,f
     2     2  a,c,e,f
     3     3      a,b
     ...
     37   37  a,c,e,f
     38   38      d,e
     39   39    a,d,f
     """
     # Cargamos el archivo, indicamos que tiene encabezado y que  \t es el separador
     table = pd.read_csv(
          "files/input/tbl1.tsv",
          header=0,
          delimiter="\t",
          index_col=None
          )



     # Agrupamos por c1, luego tomamos los valores de c4
     # aplicamos un agg que lo que hace es ir grupo por grupo, ordenar los valores y concatenarlos
     # reseteamos los indices para que c0 no quede como indice sino como columna
     # al final convertimos a df
     tableResult = pd.DataFrame(table.groupby('c0')['c4'].agg(lambda x: ','.join(sorted(x))).reset_index())
     
     return tableResult