# Calculadora em Python

operacoes = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y if y != 0 else 'Erro: divisão por zero',
}

historico = []

def calculadora(op, x, y):
    if op in operacoes:
        resultado = operacoes[op](x, y)
        historico.append(f'{x} {op} {y} = {resultado}')
        return resultado
    return 'Operação inválida'

def mostrar_historico():
    print('\n📜 Histórico de operações:')
    if not historico:
        print('Nenhuma operação realizada ainda.')
    for item in historico:
        print(item)

def limpar_historico():
    historico.clear()
    print('🧹 Histórico limpo!')

def menu():
    while True:
        print('\n🐍 Calculadora em Python 🐍')
        print('1 - Realizar operação')
        print('2 - Ver histórico')
        print('3 - Limpar histórico')
        print('0 - Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            op = input('Operação (+, -, *, /): ')
            try:
                x = float (input('Digite o primeiro número: '))
                y = float (input('Digite o segundo número: '))
                print('Resultado:', calculadora(op, x, y))
            except ValueError:
                print('❌ Entrada inválida. Use números.')
        elif escolha == '2':
            mostrar_historico()
        elif escolha == '3':
            limpar_historico()
        elif escolha == '0':
            print('👋 Saindo da calculadora...')
            break
        else:
            print('❌ Opção inválida. Tente novamente.')

menu()
