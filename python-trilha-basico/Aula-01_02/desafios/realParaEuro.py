# Faça um programa que lê um valor em reais e calcule o valor equivalente em euro. O usuário deve informar, além do valor em reais da compra, o valor da cotação do euro atual.

real = float(input('Digite o valor em reais para receber o valor equivalente em euros: '))
cotaEuro = float(input('Digite o valor do euro hoje: '))
euro = real * cotaEuro

print('O valor de %.2f em euros é: %0.2f ' % (real, euro))
