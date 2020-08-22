class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def ligar(self):
        print('estou ligando')
    
    def desligar(self):
        print('estou desligando')
    
    def trancar(self):
     print('estou trancando')

    def detalhes(self):
        print('eu sou um', self.modelo, self.cor, self.ano)


carro1 = Carro('Monza','Branco', 1995)
carro1.ligar()
carro1.desligar()
carro1.trancar()
carro1.detalhes()