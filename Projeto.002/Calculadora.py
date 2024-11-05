from time import sleep

print('''1 = Adição
2 = Subtração
3 = Multiplicação
4 = Divisão''')
while True:
    opc = input('Digite qual vai ser sua opção: ')

    if opc in ['1', '2', '3', '4']:
        N1 = float(input('Digite o primeiro valor: '))
        N2 = float(input('Digite o segundo valor: '))

        if opc == '1':
            resultado = N1 + N2
            print(f'A soma de {N1} + {N2} é igual a {resultado}')
        elif opc == '2':
            resultado = N1 - N2
            print(f'A subtração de {N1} - {N2} é igual a {resultado}')
        elif opc == '3':
            resultado = N1 * N2
            print(f'A multiplicação de {N1} x {N2} é igual a {resultado}')
        elif opc == '4':
            resultado = N1 / N2
            print(f'A divisão de {N1} / {N2} é igual a {resultado}')
        else:
            print('Erro! Tente novamente.')

    novamente = input('Deseja fazer outro calculo (s/n): ').lower()
    if novamente == 's':
        print('OK! Aguarde um momento...')
        sleep(1.5)
    elif novamente == 'n':
        print('OK! Até mais...')
        break
    else:
        print('ERRO! Tente novamente...')