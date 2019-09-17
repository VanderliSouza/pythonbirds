class Pessoa:
    def __init__(self, *filhos: object, nome: object = None, idade: object = 36) -> object:
        """

        :type filhos: object
        """
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumnprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    edie = Pessoa(nome = 'Edie')
    joao = Pessoa(edie, nome = 'Joao')
    #print(Pessoa.cumprimentar(p))
    print(id(joao))
    print(joao.cumnprimentar())
    #p.nome = "Jesus"
    print(joao.nome)
    print(joao.idade)
    for filho in joao.filhos:
        print(filho.nome)




