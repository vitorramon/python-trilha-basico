# Faça um programa que leia dois valores x e y. O programa deve trocar os valores lidos, de forma que, ao final, x contenha o valor que foi inicialmente atribuído em y, e y contenha o valor que foi inicialmente atribuído a x. Imprima os valores de x e y logo após a leitura, e depois imprima novamente após a troca.

valorA = int(input('Digite o primeiro valor: '));
valorB = int(input('Digite o segundo valor: '));

print('Valores antes da troca.')
print(valorA)
print(valorB)

temp = valorA
valorA = valorB
valorB = temp

print('Valores depois da troca.')
print(valorA)
print(valorB)

