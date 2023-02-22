# Implementação: Aplicações da Programação Funcional

*código feito em python*

Suponha que temos uma lista de produtos.
Para calcular o preço médio desses produtos, podemos utilizar a seguinte sequência de operações com map, filter e reduce:

* Utilizar o map para extrair apenas o preço de cada produto;
* Utilizar o filter para remover produtos com preços maiores que 6 reais;
* Utilizar o reduce para somar os preços e calcular a média.

A função de adicionar um produto à lista utiliza o map para transformar os valores de entrada do usuário em um dicionário com as informações do produto, e o reduce para adicionar o dicionário à lista. Já a função de remover um produto utiliza o filter para encontrar o produto a ser removido na lista e o reduce para atualizar a lista sem o produto selecionado.

Uma das principais vantagens de utilizar a programação funcional na resolução deste problema foi a facilidade de manutenção e extensão do código. As funções foram desenvolvidas de forma modular e podem ser facilmente reutilizadas em outros programas. Além disso, a aplicação dos conceitos de map, filter e reduce tornou o código mais legível e conciso, o que facilita a compreensão do que está acontecendo em cada função.

Outra vantagem é que a programação funcional possibilita a utilização de funções de ordem superior, ou seja, funções que recebem outras funções como parâmetros. Isso permite que as funções sejam mais genéricas e possam ser adaptadas a diferentes situações.

A saída desse programa será:
```java
O preço médio dos produtos é: R$ 4.30
```
