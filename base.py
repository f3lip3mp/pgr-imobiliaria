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


def add_imovel():
    imobiliaria = add_imob()
    separador()
    tipo = input('Tipo do imóvel: ')
    while True:
        try:
            if tipo == "apartamento" or tipo == "casa":
                
                endereco = input('Endereço: ')
                alugado = input('Status: ')
                while True:
                    try:
                        if alugado == "alugado" or alugado == "disponivel":
                            imobiliaria[2] = tipo
                            imobiliaria[3] = endereco
                            imobiliaria[4] = alugado
                            return imobiliaria
                    except ValueError:
                        print("Valor inválido...")
                        pass
        except ValueError:
            print("Valor inválido... somendo CASA e APARTMENTO são válidos")
            pass

def write(imobs):
    armazenamento = []
    for info_obj in imobs:
        # formata com o separador ;
        formata_imobiliaria = ';'.join(str(x) for x in info_obj.__list__()).replace(', ', ',')
        armazenamento.append(formata_imobiliaria)
    with open(arquivo_imobiliaria, 'w') as imobiliarias:
        # formata com novas linhas e grava
        imobiliarias.write('\n'.join(armazenamento))
        imobiliarias.close()

def valida_input(acao):
    try:
        cast_acao = int(acao)
        if cast_acao > 4 or cast_acao < 0:
            separador()
            print('Valor não permitido')
    except ValueError:
        separador()
        print('Valor não permitido')

def main():
    while True:
        separador()
        print('0 - Finalizar\n'
        '1 - Adicionar Imobiliaria\n'
        '2 - Adicionar Imóvel\n'
        '3 - Relatório de Imobiliárias e seus imóveis\n'
        '4 - Alterar status Alugado/Disponível')
        separador()

        input_menu = input('Escolha: ')
        valida_input(input_menu)
        if input_menu == '0':
            print('Salvando mudanças e finalizando programa...')
            # Grava as mudanças feitas pelo usuario.
            write(lst_imobiliarias)
            sys.exit(0)
        if input_menu == '1':
            # Instancia a funcão que adiciona uma nova imobiliaria.
            imob = add_imob()
            lst_imobiliarias.append(Imobiliaria(imob))
        if input_menu == '2':
            imov = add_imovel()
            lst_imobiliarias.append(Imobiliaria(imov))
        if input_menu == '3':
            separador()
            for imob in lst_imobiliarias:
                print([str(x) for x in imob.__list__()])
        if input_menu == '4':
            # Enumera e printa as as imobiliarias para que o usuario escolha.
            for index, imov in enumerate(lst_imobiliarias):
                print(index, '-', str(imov.__list__()))
            print('\n'
            '\n')
            escolha_imov = int(input('Escolha o imovel: '))
            lst_imobiliarias[escolha_imov].atualiza_imovel()


if __name__ == '__main__':
    lst_imobiliarias = [Imobiliaria(x) for x in ler_arquivo_imobiliaria()]

    try:
        # Inicia a classe main
        main()
    except KeyboardInterrupt:
        pass
