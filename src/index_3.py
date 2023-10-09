# Exemplo de estrutura condicional if-elif-else
nota = 75
if nota >= 90:
    print("Aprovado com A+.")
elif nota >= 80:
    print("Aprovado com A.")
elif nota >= 70:
    print("Aprovado com B.")
else:
    print("Reprovado.")

# Exemplo de função
def saudacao(nome):
    print("Olá,", nome)

saudacao("João")

# Exemplo de recursão
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print("Fatorial de 5:", fatorial(5))
