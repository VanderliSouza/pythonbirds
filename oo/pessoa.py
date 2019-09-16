class Pessoa:
    def __init__(self, nome=None, idade=36):
        self.idade = idade
        self.nome = nome

    def cumnprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Gustavo')
    #print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumnprimentar())
    #p.nome = "Jesus"
    print(p.nome)
    print(p.idade)




