## Algoritmos de Ordenação
 # A essência dos algoritimos de ordenação consiste em comparar dosi valores, verificar qual é menor e colocar na posição correta.
 # Em Python, existem duas formas já programdas que nos permitem ordenar uma sêquencia: a função built-in sorted() e o método sort(), presente nos objetos da classe list.

## ex: 1

lista = [10, 4, 1, 15, -3 ]

lista_ordenada_1 = sorted(lista)

lista_ordenada_2 = lista.sort()

print('lista = ', list, '/n')

print('lista_ordenada_1 = ', lista_ordenada_1)
print('lista_ordenada_2 = ', lista_ordenada_2)

print('lista = ', lista)

lista = [7, 4]

if lista[0] > lista[1]:
    aux = lista[1]
    lista[1] = lista[0]
    lista[0] = aux

print(lista)  

## ex: 2

def executar_selection_sort(lista):
    n = len(lista)
    for i in range(0, n):
        index_menor = i
    for j in range(i+1, n):
        if lista[j] < lista[index_menor]:
            index_menor = j
        lista[i], lista[index_menor] = list[index_menor], lista[i]

    return lista

lista = [10, 9, 5, 8, 11, 3]
print(executar_selection_sort(lista))
