#calculadora de combustivel
#se o valor do alcool for <= 70%(0.7) do valor da gasolina, abasteça alcool
#basta dividir o valor do litro do álcool pelo da gasolina

class Calcombustivel:
    def __init__(self):
         self.alcool = 0
         self.gasolina = 0
         self.cresultado = 0

    def Inicio(self):              
        print('*'*31)
        print('* CALCULADORA GASOLINA X ALCOOL *')
        print('*'*31)
        print('O VALOR DO ALCOOL TEM QUE SER ATÉ 70% DO VALOR DA GASOLINA ')
        Calcombustivel.Formula(self)

    def Formula(self):
        self.gasolina = float(input('Valor Gasolina: '))
        self.alcool = float(input('Valor Alcool: '))
        self.resultado = (self.alcool / self.gasolina)
        print(f'R${self.gasolina} x R${self.alcool} = {self.resultado}%')
    




start = Calcombustivel()
start.Inicio()