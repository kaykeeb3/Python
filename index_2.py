## Estrutura de Dados em Python: 

# Ojetos do tipo sequência: texto, tupla e lista.
  ## Essas estruturas de dados repesentam sequência finitas, indexadas por números não negativos.
  ## ex: uma string, que é formada por um conjuto de caracteres.
  ## Toda sequência começa com 0 e vai até n-1, que é o último valor.

# ex:
texto = "Aprendeno a linguagem de programção Python"

### len() permite saber o tamanho da sequência:
print(f"Tamanho do Texto = {len(texto)}")

### in por sua vez, permite saber se um determinado valor está ou não na sequência.  
print(f"Python in Texto = {'Python' in texto}")

### count permite contar a quantidade de ocorrência de um valor.
print(f"Quantidade de y no texto = {texto.count('y')}")

### e a notação com colchetes permite fatiar a sequência, exibindo somente partes dela: vai exibir da posição 0 até 5, pois o valor 6 não é incluso. ex: n-1.
print(f"As 5 primeiras letras são: {texto[0.6]} ")

# ex:
## Por meio de estrutura de repetição, imprimimos cada elemento da lista juntamente com seu índice. Veja a sequência possiu a função index, que retorna a posição de um valor na sequência.

## Estrutura de repetição: 
vogais = ['a', 'e', 'i', 'o', 'u'] # poderia ser utilizado as aspas duplas.

for vogal in vogais:
  print (f'Posição = {vogais.index(vogal)}, valor = {vogal}')

# ex:
texto = "Aprendeno Python na diciplina de linguagem de programação."

print(f"texto = {texto}")

print(f"Tamanho do texto = {len(texto)}/n")

# ex:

## a função split(), usada para "corta" um texto e transformá-lo em uma lista. obs: essa função pode ser usada sem nenhum parâmetro: texto.split(). Nesse caso, a string será cortada a cada espaço em branco que for encontrado. Caso seja passado um parâmetro: texto.split(","), então o corte será feito no parâmetro especificado.
   
palavras = texto.split()

print(f"palavras = {palavras}")

print(f"tamanho de palavras = {len(palavras)}")

# ex:

## List comprehesion (Compreensões de lista). A list comprehesion, também pode ser chamado de listcomp. Esse tipo de técnica é utilizada quando, dada uma sêquencia, deseja-se criar uma nova sêquencia, porém com as informações originais transformando ou filtradas por um critério.

## É uma estrutura de dados sequencial que possui características ser mútavel. Ou seja colocar dados e remover esses determinados dados.

# ex: de listas;
# lista_1 = []
# lista_2 = ['a', 'b', 'c']
# Usando o List comprehesion
# [x for x in iterable]
# list()

# ex:
linguagens = ['Python', 'C', 'C++', 'Java', 'Go', 'Ruby']

print("Antes do listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]

print("/nDepois do listcomp = ", linguagens)

# Funções: built-in são usadas por esses tipo de estrutura de dados: map() e filter()

# map() ele é usado para aplicar determinada função em cada item de um objeto iterável.

# ex:
print("Exemplos")

linguagens = '''Python Java Javascript C# Go C'''.split()
nova_lista = map(lambda x: x.lower(), linguagens) ## lambda é uma função chamada uma vez.
print(f"A nova lista é = {nova_lista}/n")
nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é = {nova_lista}")

# ex:
numeros = list(range(0, 21))

numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))

print(numeros_pares)

## Tupas não são mutavel, logo não podemos acessar os items.

vogais = ('a', 'e', 'i', 'o', 'u')
print(f"Tipo de objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
  print(f"Posição = {p}, valor = {x}")


# Objetos do tipo set(conjunto).
  ## Tradução "conjunto", vai possibilitar a trabalhar com diversas operações matemáticas.
  ## Chamamos de conjunto toda e qualquer coleção de elementos. Estes elementos podem ser números, objetos, figuras, pessoas, animais e tudo o que podemos ordenar, catalogar ou reunir em grupos de seus elementos.


# Objetos do tipo mapping (dicionário).
  ## As estruturas que possuem um mapeamento entre uma chave e um valor são considerados objetos do tipo "mapping".
  
# ex: 1 - Criação de um dicionário vazio, com atribuição posterior de uma chave valo:
dici_1 = {}
dici_1['nome'] = "João"
dici_1['idade'] = 25

# ex: 2 - Criação de um dicionário usando um par elementos na forma, chave: valor
dici_2 = {'nome': 'João', 'idade': 30}

# ex: 3 - Criação de um dicionário com uma lista de tuplas. Cada tupla representa um par de chave:valor
dici_3 = dict([('nome', 'João'), ('idade', 30)])

# Objetos do tipo array NumPy.
  ## O caso do NumPy criado especificamente para computação científica com Python. Para inteligência artificial: matriz (array).

## importando a biblioteca: numpy
import numpy

## ex: matriz
matriz_1_1 = numpy.array([1, 2, 3]) # cria uma matriz 1 linha 1 coluna.
matriz_2_2= numpy.array([1, 2], [3, 4]) # cria uma matriz 2 linha 2 coluna.
matriz_3_2= numpy.array([1, 2], [3, 4], [5, 6]) # cria uma matriz 3 linha 2 coluna.
matriz_2_3= numpy.array([1, 2, 3], [4, 5, 6]) # cria uma matriz 2 linha 3 coluna.

print(type(matriz_1_1))
print('n/ matriz_1_1 = ', matriz_1_1)
print('n/ matriz_2_2 = /n', matriz_2_2)
print('n/ matriz_3_2 = /n', matriz_3_2)
print('n/ matriz_2_3 = /n', matriz_2_3)