from time import sleep
print(f'{"Tabela IMC":=^40}')
sleep(1)
print('-='*20)
s = input('Diga seu sexo: H / M: ').upper()
i = int(input('Digite sua idade: '))
a = float(input('Qual é sua altura: '))
p = float(input('Qual é seu peso: '))
print('PROCESSANDO...')
sleep(2)
imc = p / (a*a)
hcond = (72.7 * a) - 58
mcond = (62.1*a)-44.7
hdif = p - hcond
mdif = p - mcond
print(f'Seu imc é: {imc:.2f}')
if imc < 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print('Peso ideal')
elif imc <= 30:
    print('Sobrepeso')
elif imc <= 35:
    print('Obesidade')
elif imc <= 39.9:
    print('ObesidadeII')
else:
    print('ObesidadeIII')
if s == 'H':
    print('Sexo Masculino')
    print(f'Seu peso ideal é: {hcond:.2f} kg')
    if p > hcond:
        print(f'Você está {hdif:.2f} kg acima do seu peso ideal')
    elif p < hcond:
        print(f'Você está {hdif:.2f} kg abaixo do seu peso ideal')
    else:
        print('PARABÉNS!!!!, você está no peso padrão')
elif s == 'M':
    print('Sexo Feminino')
    print(f'Seu peso ideal é:{mcond:.2f} kg')
    if p > mcond:
        print(f'Você está {mdif:.2f} kg acima seu peso ideal')
    elif p < mcond:
        print(f'Você esta {mdif:.2f} kg abaixo do seu peso ideal')
    else:
        print('PARABÉNS!!!!, você está no peso padrão')



