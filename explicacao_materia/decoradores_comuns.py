# Decoradores comuns são: @classmethod e @staticmethod 

class MinhaClasse:
  valor = 10  #Atributo de classe 
  def __init__(self, nome) -> None:
    self.nome = nome # Definir um atributo da instância. 

  # Requer uma instância para ser chamado. 
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.nome}"
  
  @classmethod #Recebe a referência da classe. 
  def metodo_classe(cls):
    return f"Método da classe chamado para valor={cls.valor}"
  # Com esse método consigo acessar o valor(atributo da classe) mas não consigo acessar o nome(atributo da instância)

  @staticmethod #Não recebe referência. 
  def metodo_estatico():
    return "Método estático chamado"

  # Diferente dos métodos da intância e da classe pq ele não recebe argumento, não acessa o valor da instância e nem da classe. 
    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.valor)
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

""" Onde iremos utilizar esses métodos? 
Por exemplo, o método da classe é muito usado para se criar instâncias, a partir de configurações globais. 
"""

class Carro: 
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo 
    self.ano = ano
    
  @classmethod
  def criar_carro(cls, configuração): 
    marca, modelo, ano = configuração.split(",")
    return cls(marca, modelo, int(ano))
  
configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

""" O staticmethod geralmente é utilizado em bibliotecas """

class Matematica:

  @staticmethod
  def somar(a, b):
    return a + b

print(Matematica.somar(a=10, b=15))