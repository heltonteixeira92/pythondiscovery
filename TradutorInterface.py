#TRADUTOR DE QUALQUER IDIOMA PARA INGLÊS COM INTERFACE GRÁFICA

import PySimpleGUI as sg
from googletrans import Translator

class Translator1:
    def __init__(self):
        self.frase = ''
        
    
    def Inicio(self):
        #layout
        layout = [
            [sg.Text('TEXTO'), sg.Input(key = 'frase')],
            [sg.Text('', size=(30,1), key= 'dt')],
            [sg.Text('TRADUÇÃO')],
            [sg.Output(size=(30,5), key='output')],
            [sg.Button('TRADUZIR'), sg.Exit('Fechar')]
        ]
        #janela
        window = sg.Window('Translator', layout)
        #coletar dados
        while True: #vai monter o programa rodando até eu escolher sair.
            event, value = window.Read()
            translator = Translator()
         #fazer algo c dados    
            if event == 'TRADUZIR':
                try:
                    self.frase = str(value['frase'])
                    dt = translator.detect(self.frase) #vai detectar o idioma da váriavel text
                    translated = translator.translate(self.frase) #translated vai receber o text traduzido
                except:
                    output = 'invalid'
                window['output'].update(translated.text)
                window['dt'].update(dt)    
            else:
                break
        

tradutor1 = Translator1()
tradutor1.Inicio()