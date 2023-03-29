# Mudança de tipo 
# Pode-se usar: int(), float() ou eval() para fazer o python ler variáveis de tipo numérico

altura = int(input('Digite a altura do triângulo: '));
print(type(altura));
base = int(input('Digite a base do triângulo: '));
print(type(base));
area = (base * altura)/2;
print('A área do triângulo é: ', area);
