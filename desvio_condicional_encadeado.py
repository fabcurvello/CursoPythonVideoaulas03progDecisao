'''
Crie um programa que pergunte um número ao usuário.
Em seguida o programa deve informar se o número inserido está abaixo de 100,
entre 100 e 200 ou acima de 200.
'''

numero = int(input("Digite um número: "))

if ( numero < 100 ):
    print(f"{numero} está abaixo de 100.")
else:
    #garantido que o número vale pelo menos 100
    if ( numero <= 200 ):
        print(f"{numero} está entre 100 e 200.")
    else:
        print(f"{numero} está acima de 200.")