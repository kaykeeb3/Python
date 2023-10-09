# Exemplo de criação de conjunto
conjunto = {1, 2, 3, 4, 5}

# Adição de elemento a um conjunto
conjunto.add(6)

# Remoção de elemento de um conjunto
conjunto.remove(3)

# Verificação de pertencimento
if 4 in conjunto:
    print("O número 4 está no conjunto.")

# Operações de conjunto
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)
intersecao = conjunto1.intersection(conjunto2)

print("União:", uniao)
print("Interseção:", intersecao)
