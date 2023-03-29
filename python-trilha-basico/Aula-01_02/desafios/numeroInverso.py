# 2 - Faça um programa que leia 3 valores e mostre a soma de seus inversos.

num1 = float(input('Digite o primeiro número: '));
num2 = float(input('Digite o segundo número: '));
num3 = float(input('Digite o terceiro número: '));

inv1 = 1 / num1;
inv2 = 1 / num2;
inv3 = 1 / num3;

somaInv = inv1 + inv2 + inv3;

print('O resultado da soma dos inversos é: %.2f' % somaInv);

