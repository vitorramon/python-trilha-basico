# Formatação de Números
# É possível especificar uma máscara no comando print para imprimir números
# com um determinado formato.
# Ex: Fazer um float ser exibido com apenas duas casas decimais

# print('%.2f' % variável) // f para float, d para int, s para strings

altura = int(input('Digite a altura do triângulo: '));
base = int(input('Digite a base do triângulo: '));
area = (base * altura) / 2;

print('Altura = %d' % altura);
print('Base = %d' % base);
print('A área do triângulo com altura de %.0f e base %.0f é: %.2f' % (altura, base, area));



