lado1 = float(input('digte um numero para ser o lado 1 do triangulo:  '))
lado2 = float(input('digte um numero para ser o lado 2 do triangulo:  '))
lado3 = float(input('digte um numero para ser o lado 3 do triangulo:  '))

if lado1 + lado2 == lado3:
    print('')
elif lado1 == lado2 == lado3:
    print('esse triangulo é equilatero')