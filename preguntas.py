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

    A4=tbl0.groupby('_c1')['_c2'].mean()
    return A4
    
#Answer_4=print(pregunta_04())


def pregunta_05():

    A5=tbl0.groupby('_c1')['_c2'].max()
    return A5

#Answer_5=print(pregunta_05())


def pregunta_06():

    A6=tbl1['_c4'].unique()
    A6=[element.upper() for element in A6]
    A6=sorted(A6)
    return A6

#Answer_6=print(pregunta_06())


def pregunta_07():

    A7=tbl0.groupby('_c1')['_c2'].sum()
    return A7

#Answer_7=print(pregunta_07())


def pregunta_08():

    tbl0['suma']=tbl0['_c0']+tbl0['_c2']
    return tbl0

#Answer_8=print(pregunta_08())


def pregunta_09():

    tbl0['year']=tbl0['_c3'].str.split('-').str[0]
    return tbl0
   
#Answer_9=print(pregunta_09())


def pregunta_10():

    A10=tbl0.groupby('_c1')['_c2'].apply(lambda x: ':'.join(sorted(x.astype(str))))
    A10.columns=['_c0', '_c1']
    A10=pd.DataFrame(A10)
    return A10

#Answer_10=print(pregunta_10())


def pregunta_11():

    A11=tbl1.groupby('_c0')['_c4'].apply(lambda x: ','.join(sorted(x))).reset_index()
    A11.columns=['_c0', '_c4']
    return A11
    
#Answer_11=print(pregunta_11())


def pregunta_12():

    tbl2['_c5']=tbl2['_c5a']+':'+tbl2['_c5b'].astype(str)
    A12=tbl2.groupby('_c0')['_c5'].apply(lambda x: ','.join(sorted(x))).reset_index()
    return A12
   
#Answer_12=print(pregunta_12())



def pregunta_13():
   
    combined = pd.merge(tbl0, tbl2, on='_c0')
    A13=combined.groupby('_c1')['_c5b'].sum()
    return A13

#Answer_13=print(pregunta_13())
