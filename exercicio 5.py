n1 = float(input('digite um numero para calcular: '))
op = input('digite uma operação')
n2 = float(input('digite outro numero para calcular: '))

if op == '+':
    print(n1 + n2)
elif op == '-':
    print(n1 - n2)
elif op == '*':
    print(n1 * n2)
elif op == '/':
    print(n1 / n2)
else:
    print('digite uma operação valida')