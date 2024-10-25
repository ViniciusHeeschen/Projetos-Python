from random import randint
from time import sleep

#cores letras
VERDE = '\033[32m'
VERMELHO = '\033[31m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
RESET = '\033[0m'

#cores fundos
FUNDO_VERMELHO = '\033[41m'
FUNDO_VERDE = '\033[42m'
FUNDO_AZUL = '\033[44m'
FUNDO_AMARELO = '\033[43m'

while True:
    print('''
    [ 1 ] \033[43mPedra\033[0m
    [ 2 ] \033[43mPapel\033[0m
    [ 3 ] \033[43mTesoura\033[0m''')
    jogador = int(input('Qual vai ser sua Opção:'))
    computador = randint(1,3)

    sleep(1)
    print('\033[33mJO\033[0m')
    sleep(1)
    print('\033[33mKENN\033[0m')
    sleep(1)
    print('\033[33mPOOOO\033[0m')

    if computador == 1:
        if jogador == 1:
            print('\033[34mEMPATE!\033[0m')
        elif jogador == 2:
            print('\033[32mJOGADOR VENCEU!\033[0m')
        elif jogador == 3:
            print('\033[31mCOMPUTADOR VENCEU!\033[0m')
    if computador == 2:
        if jogador == 1:
            print('\033[31mCOMPUTADOR VENCEU!\033[0m')
        elif jogador == 2:
            print('\033[34mEMPATE!\033[0m')
        elif jogador == 3:
            print('\033[32mJOGADOR VENCEU!\033[0m')
    if computador == 3:
        if jogador == 1:
            print('\033[32mJOGADOR VENCEU!\033[0m')
        elif jogador == 2:
            print('\033[31mCOMPUTADOR VENCEU!\033[0m')
        elif jogador == 3:
            print('\033[34mEMPATE!\033[0m')

    while True:
        jogar_novamente = input('Deseja jogar Novamente (s/n): ').lower()
        if jogar_novamente in ['s', 'n']:
            break
        else:
            print("\033[41mInválidado! Digite 's' para sim ou 'n' para não\033[0m")
    if jogar_novamente == 'n':
        print('\033[44mObrigado por Jogar!\033[0m')
        break
print('Fim!')
