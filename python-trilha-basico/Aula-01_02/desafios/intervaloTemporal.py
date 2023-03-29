# Faça um programa que transforme o valor correspondente a um intervalo temporal, expresso em horas, minutos e segundos, no valor correspondente em segundos.

horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))

totalSegundo = horas * 3600 + minutos * 60 + segundos

print('O total do horário descrito em segundos é: %d' % totalSegundo)