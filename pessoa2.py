class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        return f'''
        Nome: {self.nome}
        Idade: {self.idade}
        '''

gabriel = Pessoa('Gabriel', 30)
print(gabriel.info())
