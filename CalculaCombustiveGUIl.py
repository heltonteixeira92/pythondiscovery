#calculadora de combustivel com interface
#se o valor do alcool for < 70%  do valor da gasolina, abasteça alcool
#basta dividir o valor do litro do álcool pelo da gasolina < 0.7 ruim, >= 0.7 bom.
import PySimpleGUI as sg

class Calcombustivel:
    def __init__(self):
         alcool = 0
         gasolina = 0
         resultado = 0

    def Inicio(self):
        #layout
        layout = [
            [sg.Text('*'*40)],
            [sg.Text('* Calculadora Gasolina x Alcool *')],
            [sg.Text('*'*40)],
            [sg.Text('Alcool R$:'), sg.Input(key = 'alcool')],
            [sg.Text('Gasolina R$:'), sg.Input(key = 'gasolina')],
            [sg.Text('', size=(8,1), key = 'output')],
            [sg.Button('Calcular', bind_return_key = True),sg.Exit('Sair')],
            
        ]
        #janela
        window = sg.Window('Alcool x Gasolina', layout)
        
        
       
        while True:  
            event, values = window.Read()  #extrair dados            
            if event == 'Calcular':
                try:
                    gasolina = float(values['gasolina'])    # fazer algo com dados
                    alcool = float(values['alcool'])
                    resultado = alcool / gasolina
                    
                    
                except:
                    resultado = 'invalid'

                window['output'].update(resultado)
            else:
                break    
                
        #window.close()
        

   
    




start = Calcombustivel()
start.Inicio()
