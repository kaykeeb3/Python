# Exemplo 1

lista = [10, 4, 1, 15, -3]

lista_ordenada_1 = sorted(lista)

lista.sort()  # Use o método sort() em vez de lista.sort() para ordenar a lista in-place

print('lista = ', lista)  # Corrigido '\n' para '\n'

print('lista_ordenada_1 = ', lista_ordenada_1)
print('lista_ordenada_2 = ', lista)  # Use 'lista' em vez de 'lista_ordenada_2'

lista = [7, 4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)

# Exemplo 2

def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
        for j in range(i + 1, n):  # Corrigido a indentação deste loop
            if lista[j] < lista[index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]  # Corrigido 'list' para 'lista'

    return lista

lista = [10, 9, 5, 8, 11, 3]
print(executar_selection_sort(lista))
