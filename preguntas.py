"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""

import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():

    a = tbl0.shape[0]
    return a



def pregunta_02():
    
    a = tbl0.shape[1]
    return a



def pregunta_03():

    return tbl0["_c1"].value_counts().sort_index()




def pregunta_04():

    return tbl0.groupby("_c1")["_c2"].mean().sort_index()

    
#Answer_4=print(pregunta_04())


def pregunta_05():

    return tbl0.groupby("_c1")["_c2"].max().sort_index()


#Answer_5=print(pregunta_05())


def pregunta_06():

    return  tbl1["_c4"].str.upper().sort_values().unique().tolist()


#Answer_6=print(pregunta_06())


def pregunta_07():

    return tbl0.groupby("_c1")["_c2"].sum().sort_index()
   

#Answer_7=print(pregunta_07())


def pregunta_08():

    a = tbl0["_c0"] + tbl0["_c2"]
    return tbl0.assign(suma=a)

#Answer_8=print(pregunta_08())


def pregunta_09():

    return tbl0.assign(year=tbl0["_c3"].str.split("-").str[0])

   
#Answer_9=print(pregunta_09())


def pregunta_10():

    table=tbl0.groupby("_c1")["_c2"].apply(lambda x: ":".join(map(str, sorted(list(x)))))
    df = pd.DataFrame(table)
    
    return df

#Answer_10=print(pregunta_10())


def pregunta_11():

    table = tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(sorted(x)))
    table = table.reset_index()
    return table
    
#Answer_11=print(pregunta_11())


def pregunta_12():

    return tbl2.groupby("_c0").apply(lambda x: ",".join(sorted(x["_c5a"] + ":" + x["_c5b"].astype(str)))).reset_index().rename(columns={0:"_c5"})

   
#Answer_12=print(pregunta_12())



def pregunta_13():
   
    tbl = tbl0[["_c0", "_c1"]]
    table = pd.merge(tbl, tbl2, sort=True)
    table = table.groupby("_c1")["_c5b"].sum()
    return table

#Answer_13=print(pregunta_13())
