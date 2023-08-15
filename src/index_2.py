def main():
    vetor = []
    for i in range(5):
        numero = int(input(f"Digite o {i+1}° número inteiro: "))
        vetor.append(numero)

    soma = sum(vetor)
    mutiplicacao = 1
    for num in vetor:
        mutiplicacao *= num 

print("Números digitados:", vetor)
print("Soma:", soma)
print("Soma:", mutiplicacao)

if __name__ == "__name__":
    main()