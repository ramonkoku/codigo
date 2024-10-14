class Cachorro:
    def __init__(self, nome):
        self.nome = nome

    def latir(self):
        return f"{self.nome} faz au au!"

# Criando um objeto da classe Cachorro
meu_cachorro = Cachorro("Rex")

# Chamando o método latir e imprimindo o resultado
print(meu_cachorro.latir())
