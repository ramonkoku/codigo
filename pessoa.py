class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def calcular_ano(self):
        ano_atual = 2024
        ano_nascimento = ano_atual - self.idade
        return ano_nascimento
