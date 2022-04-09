import os
import sys

from os.path import join


 
arquivo_imobiliaria = join('imobiliarias.txt')

def ler_arquivo_imobiliaria():
    lista_imobiliarias = []
    with open(arquivo_imobiliaria, 'r') as imobiliarias:
        for x in imobiliarias.readlines():
            # Separa o elementos pelo separador ; e remove espaços
            lista_imobiliarias.append(x.strip().split(';'))
        imobiliarias.close()
    return lista_imobiliarias