import time
from class_navegador import Navegador
from class_pesquisa_usuario import PesquisaUsuario


def solicitando_as_informacoes():
    print('----INFORMAÇÕES DO RESULTADO---')
    latitude = input('Informe a Latitude: ')
    longitude = input('Informe a Longitude: ')
    print('')
    print('----INFORMAÇÕES DO USUÁRIO---')
    pesquisa_realizada = input('Pesquisa Realizada Pelo Usuário: ')
    print('')

    return latitude, longitude, pesquisa_realizada


def execucao_final():
    latitude, longitude, pesquisa_realizada = solicitando_as_informacoes()
    pesquisando_coordenadas = Navegador('https://www.google.com/maps')
    pesquisando_coordenadas.pesquisando(f'{latitude}, {longitude}',
                                        '//input[@id="searchboxinput"]')
    pesquisando_coordenadas.obtendo_link()

    pesquisa_do_usuario = PesquisaUsuario('https://www.google.com/')
    pesquisa_do_usuario.realizando_pesquisa(pesquisa_realizada, 'q')


def menu_de_opcoes():
    print('')
    print('1 - Pesquisar novamente\n'
          '2 - Fechar o programa')


def main():
    execucao_final()
    while True:
        menu_de_opcoes()
        escolha_do_usuario = input('Escolha uma das opções: ')
        if escolha_do_usuario == '1':
            execucao_final()
        elif escolha_do_usuario == '2':
            print('Programa Será Finalizado.')
            time.sleep(2)
            break
        else:
            print('Opção Inválida, tente novamente!')


if __name__ == '__main__':
    main()
