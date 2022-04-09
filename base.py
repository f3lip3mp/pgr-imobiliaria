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

class Imovel():
    def __init__(self, imov):
        super(Imovel, self).__init__()
        # Recebe os dados do imovel e alimenta os atributos da classe
        self.tipo = imov[0]
        self.endereco = imov[1]
        # Modifica o status de aluguel para buleano
        self.alugado = True if imov[2] == 'ALUGADO' else False