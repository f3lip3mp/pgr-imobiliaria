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

    def atualiza_status(self):
        #atualiza o status de aluguel
        if self.alugado is True:
            self.alugado = False
        elif self.alugado is False:
            self.alugado = True

    def __list__(self):
        return [self.tipo, self.endereco, 'ALUGADO' if self.alugado else 'DISPONIVEL']


class Imobiliaria():
    def __init__(self, imob):
        super(Imobiliaria, self).__init__()
        self.nome_imobiliaria = imob[0]
        self.telefones = str(imob[1])
        self.__lst_imoveis_alugar = Imovel(imob[2:])

    def atualiza_imovel(self):
        # chamando o metodo atualiza_status que atualiza o status de aluguel
        self.__lst_imoveis_alugar.atualiza_status()

    def __list__(self):
        # retorna uma lista com os atributos da imobiliaria, tendo ou não um imovel
        return [self.nome_imobiliaria, self.telefones] + self.__lst_imoveis_alugar.__list__()


def separador():
    print("=*"*30)


def add_imob():
    separador()
    imob = input('Nome da Imobiliária: ')
    for x in range(0, 1):
        fone = input(f'Telefone: ')
    return [imob, fone, 'null', 'null', 'null']