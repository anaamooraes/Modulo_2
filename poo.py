# POO(Programação Orientada a Objetos): existem linguagens de programação que adotam e implementam os principios e conceitos da POO, linguagens como Python, Java, C++, C Shar e Ruby, permitem que os programadores criem softwares de forma modular, reutilizavel e mais facil de entender e manter. A POO é um paradigma de programação que se baseia na organização dos programas em torno de objetos, que são instancias de classes. Dentro das classes, podemos descrever atributos e métodos, que são ações que os objetos podem realizar. O construtor é um método especial que nos permite definir os atributos da classe. 

# Classes: Uma classe é um modelo, um plano que define a estrutura e o comportamento dos objetos. (atributos e metodos)

# Para criarmos um classe: 
class Pessoa:
  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Um objeto é uma instancia da classe, é criado a partir de uma classe. 
pessoa1 = Pessoa("Ana", 26)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Helena", 1)
mensagem = pessoa2.saudacao()
print(mensagem)