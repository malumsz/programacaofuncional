from functools import reduce

produtos = [('arroz', 10.50), ('feijão', 6.75), ('macarrão', 4.99), ('óleo', 5.20), ('açúcar', 2.49)]

# Utilizar o map para extrair apenas o preço de cada produto
precos = map(lambda p: p[1], produtos)

# Utilizar o filter para remover produtos com preços maiores que 6 reais
precos_filt = filter(lambda p: p <= 6.0, precos)

# Utilizar o reduce para somar os preços e calcular a média
soma = reduce(lambda acc, p: acc + p, precos_filt, 0)
media = soma / len(produtos)

print(f'O preço médio dos produtos é: R$ {media:.2f}')
