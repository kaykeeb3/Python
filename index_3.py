## Conceitos de orientação a objetos:
  # Uma classe é uma abstração que escreve entidades do mundo real e quando instanciadas dão origem a objetos. Portanto, a classe é o modelo e o objeto é uma instância. 

# Atributos:
  # São os dados armazenados em um objeto representam o estado do objeto, são as características.

# Herança:
  # Por meio desse mecanismo, é possível fazer o reuso de códico, criando soluções mais organizadas. Permite que uma classe herde os atributos e métodos de outra classe.

# Encapsulamento:
  # O ato de combinar os atributos e métodos na mesma entidade. Isso é chamado de "Ocultação da Informação".

# Polimorfismo:
  # Significa "muitas formas", usar o mesmo elemento de formas diferentes.

## Classes e métodos em Python:

# ex:
class PrimeraClasse:
    
    def imprimir_mensagem(self, nome): # criando um método
        print(f"Olá {nome}, seja bem vindo!")
        objeto_1 = PrimeraClasse() # instanciando um objeto do tipo PrimeraClasse
        objeto_1.imprimir_mensagem('João') # invocando o método