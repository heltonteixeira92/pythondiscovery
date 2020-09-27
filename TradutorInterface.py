#TRADUTOR DE QUALQUER IDIOMA PARA INGLÊS COM INTERFACE GRÁFICA

import PySimpleGUI as sg
from googletrans import Translator

class Translator1:
    def __init__(self):
        self.frase = ''

    def about_me(self):
        '''about'''
        sg.popup_no_wait(' hello word, testando o menu about', auto_close=False)

    def Inicio(self):
        #layout

        menu_layout = [
            ['Help', ['About']]
        ]

        layout = [
            [sg.Menu(menu_layout)],
            [sg.Text('TEXTO')],
            [sg.Multiline(key = 'frase',size=(30,5))],
            [sg.Text('', size=(30,1), key= 'dt')],
            [sg.Text('TRADUÇÃO')],
            [sg.Output(size=(30,5), key='output')],
            [sg.Text('Select Language '),sg.InputCombo(('pt', 'en'), key='language')],
            [sg.Button('TRADUZIR'), sg.Exit('Exit')]
        ]
        
        #janela
        window = sg.Window('Translator', layout)
        
        #coletar dados
        while True: #vai monter o programa rodando até eu escolher sair.
            event, value = window.Read()
            translator = Translator()
         #fazer algo c dados 
            if event in ('Exit', None):
                break   
            if event in ('About',):
                self.about_me()
            if event in 'TRADUZIR':
                try:
                    language = value['language'] #pega o valor do ComboxBox
                    self.frase = str(value['frase']) #pega o valor input text
                    dt = translator.detect(self.frase) #vai detectar o idioma da váriavel text
                    translated = translator.translate(self.frase, dest = language) #translated vai receber o text traduzido
                except:
                    output = 'invalid'
                window['output'].update(translated.text)
                window['dt'].update(dt)    
            
        

tradutor1 = Translator1()
tradutor1.Inicio()