peso = float(input('qual seu peso: '))
altura = float(input('qual a sua altura: '))

imc = peso/altura

if imc < 18.5:
    print('abaixo do peso')
elif imc >= 18.5 and imc < 24.9:
    print('Peso normal')
elif imc >= 25 and imc < 29.9:
    print('sobrepeso')
elif imc >=30:
    print('obeidade')
