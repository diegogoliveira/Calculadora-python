from funcoes import adicao, subtracao, divisao, multiplicacao
while True:
    print('Olá insira os dados abaixo.')
    operador = str(input('insira o operador desejado\n+\n-\n*\n/\nOu digite sair para encerrar.: '))
    if operador == 'sair':
        print('Operação finalizada')
        break

    x = float(input(' Insira o primeiro valor da operação.\n:'))
    y = float(input('Insira o segundo valor da operação.\n'))

    if operador == '+':
        print('Resultado é: ', adicao(x, y))

    elif operador == '-':
        print('Resultado é: ', subtracao(x, y))

    elif operador == '/':
        print('Resultado é: ', divisao(x, y))

    elif operador == '*':
        print('Resultado é: ', multiplicacao(x, y))

    else:
        print("não entendi a operação!\nVamos tentar novamente ?\n")



