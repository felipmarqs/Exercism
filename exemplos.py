class Produto():
    def __init__(self, nome, preco):
        self.nome = nome
        self.__preco = preco
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self,novo_valor):
        if novo_valor > 0:
            self.__preco = novo_valor
        return self.preco

    def reajustar(self, percentual):
        percentual = 1 + percentual / 100
        self.preco *= percentual
    
    def __repr__(self):
        return self.nome

    def __str__(self):
        return f'{self.nome.upper()} -- {self.preco:.2f} '

if __name__ == '__main__':
    print('Não me execute.')
