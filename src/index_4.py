# Exemplo de definição de classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, eu sou", self.nome, "e tenho", self.idade, "anos.")

# Instanciando um objeto da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pessoa1.apresentar()
pessoa2.apresentar()

# Exemplo de herança de classes
class Estudante(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("Olá, eu sou", self.nome, "e tenho", self.idade, "anos. Minha matrícula é", self.matricula)

estudante = Estudante("Carol", 20, "12345")
estudante.apresentar()
