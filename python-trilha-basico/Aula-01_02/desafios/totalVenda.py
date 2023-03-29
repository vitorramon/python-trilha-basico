# Faça um programa que lê o nome de um produto, a quantidade comprada, o valor unitário e o percentual de desconto a ser aplicado para o pagamento. Imprima na tela o nome do produto e o valor total da venda.

produto = input('Digite o nome do produto: ');
qtdProd = int(input('Digite quantas unidades foram compradas de %s ' % produto));
valorUn = float(input('Digite o valor do %s ' % produto))
perDesconto = float(input('Digite o percentual de desconto a ser aplicado: '));

desconto = perDesconto / 100;
valorDesc = valorUn * desconto;

valorTotal = (valorUn - valorDesc) * qtdProd;

print('O produto é %s e o valor total da venda foi %.2f' % (produto, valorTotal));


