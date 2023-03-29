# Faça um programa para, a partir de um valor informado em centavos, indicar a menor quantidade de moedas que representa esse valor :

valor = int(input('Digite o valor em centavos: '))

moedas1R = valor // 100
valor = valor % 100

moedas50 = valor // 50
valor = valor % 50

moedas25 = valor // 25
valor = valor % 25

moedas10 = valor // 10
valor = valor % 10

moedas5 = valor // 5
valor = valor % 5

moedas1 = valor 

print(moedas1R, "moedas de 1 real")
print(moedas50, "moedas de 50 centavos")
print(moedas25, "moedas de 25 centavos")
print(moedas10, "moedas de 10 centavos")
print(moedas5, "moedas de 5 centavos")
print(moedas1, "moedas de 1 centavo")