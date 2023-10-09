# Algoritmo de Busca:
def executar_busca_binaria(lista, valor):
    lista.sort()  # Certifique-se de que a lista esteja ordenada
    minimo = 0
    maximo = len(lista) - 1  # Subtrai 1 para o índice máximo correto

    while minimo <= maximo:
        # Encontra o elemento que divide a lista ao meio
        meio = (minimo + maximo) // 2
        # Verifica se o valor procurado está à esquerda ou à direita do valor central
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor > lista[meio]:
            minimo = meio + 1
        else:
            return True  # Se o valor for encontrado, retorna True

    return False  # Se chegar até aqui, significa que o valor não foi encontrado.

# Exemplo de uso:
nomes = 'Kayke Marcela Lucas Felipe Marcos Luiza Raquel Romário João Alison Bruno'.split()
print('Marcela' in nomes)
print('Fernanda' in nomes)  # Corrigido o nome 'Fernanda'
