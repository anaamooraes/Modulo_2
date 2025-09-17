class Carro: 
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo 
    self.ano = ano
    
  @classmethod
  def criar_carro(cls, configuração): 
    marca, modelo, ano = configuração.split(",")
    
  configuracao1 = "Toyota,Corolla,2022"
