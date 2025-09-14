# Herança:
print("\nExemplo da classe herança:") 
class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def andar(self):
    print(f"O animal {self.nome} andou")
    return
  
  def emitir_som(self):
    pass 

class Cachorro(Animal): 
  def emitir_som(self):
    return "Au, Au"
  
class Gato(Animal):
  def emitir_som(self):
    return "Miau!"
  
# Polimorfismo: nos ajuda a utilizar o mesmo método definido pela classe mãe só que implementado de outra forma. 
print("\nUtilizando o Polimorfismo para realizar uma implementação diferente em cada método:")

dog = Cachorro(nome= "Claudia")
cat = Gato(nome= "Sebastião")

animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz: {animal.emitir_som()}")

# Encapsulamento: uso de atributos privados .__  
print("Exemplo de encapsulamento:")
class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo #Atributo privado: dois anderlines após o ponto.

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo
  
conta = ContaBancaria(saldo= 1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor= 500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=- 500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor= 200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# se eu quiser criar uma outra conta bancaria? 
''' conta_do_zezinho = ContaBancaria(saldo=50)'''

# Abstração: criar molde para se construir classes, nos ajuda a proteger as caracteristicas.

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC): 

  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self) -> None: 
    pass

  def ligar(self):
    return "Carro ligado usando a chave"
  
  def desligar(self):
    return "Desligado usando a chave"
  
carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())  