## Algoritmos de busca:
  ## Esse universo, como o nome já sujere, os algoritmos resolvem problemas relacionados a estrutura de dados.

# ex:

nomes = 'Kayke Marcela Lucas Felipe Marcos Luiza Raquel Romário João Alison Bruno'.split()

print('Marcela' in nomes)
print('Ferdanda')

## Busca linear (ou busca Sequencial).
  ## Percorre os elementos da sequência procura aquele de destino, começa por uma das extremidades da sequência e vai percorrendo até encontrar (ou não) o valor desejado.


## Complexidade :
 ## Em termos conputacionais, um algoritimo é considerado melhor do que o outro quando, para a  mesma entrada, utilizar menos recuros computacionais em termos de mémoria e processamento.
 ## Análise computacional é feita com duas dimensões: espaço e tempo.


# Algoritmo de Busca:
def executar_busca_binaria(lista, valor):
    minimo = 0
    maximo = len(lista)

    while minimo <= maximo:
    # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
    # Verifica se o valor procurado está a esquerda ou direita do valor central
    if valor < lista[meio]:
        maximo = meio - 1
    elif valor > lista[meio]:
        minimo = meio + 1
    else:
        return True # Se o valor for encontrado para aqui:
    
    return False # Se chegar até aqui, significa que o valor não foi encontrado.

