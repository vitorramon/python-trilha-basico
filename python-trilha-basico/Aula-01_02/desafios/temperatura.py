# 1 - Faça um programa que transforme uma temperatura fornecida em Celsius para a correspondente em Fahrenheit. A formula de conversão de Celsius para Fahrenheit é a seguinte: F = C * (9/5) + 32

celsius = int(input('Digite a temperatura em Celsius: '))
fahrenheit = celsius * 1.8 + 32;

print('A conversão da temperatura %dº em Celsius para Fahrenheit é: %dº' % (celsius, fahrenheit));