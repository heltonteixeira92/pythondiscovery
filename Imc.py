#Calculadora IMC(índice massa corpórea) peso do pasciente / altura elevado ao quadrado.
'''MENOR QUE 18,5	MAGREZA	0
ENTRE 18,5 E 24,9	NORMAL	0
ENTRE 25,0 E 29,9	SOBREPESO	I
ENTRE 30,0 E 39,9	OBESIDADE	II
MAIOR QUE 40,0	OBESIDADE GRAVE	III     '''

import PySimpleGUI as sg

class Imc:
    def __init__(self):
    #layout
        layout = [
            [sg.Text('Calculadora IMC')],
            [sg.Text('Peso: '), sg.Input(key='peso')],
            [sg.Text('altura: '), sg.Input(key='altura')],
            [sg.Button('OK')]
        ]
        self.Janela = sg.Window('Calculadora IMC', layout)
    #janela
    def Iniciar(self):
        while True:
            event, values = self.Janela.read()    #coletar dados
            if event in 'Exit' or None:
                break
            if event in 'OK':
                peso = int(values['peso'])#fazer algo com dados
                altura = float(values['altura'])
                imc = round( peso/(altura**2),2)
                if imc < 18.5:
                    sg.popup_no_wait(f'{imc}\nClassificação: Magreza')
                elif imc > 18.5 and imc < 24.9:
                    sg.popup_no_wait(f'{imc}\nClassificação: Normal')
                elif imc > 25.0 and imc < 29.9:
                    sg.popup_no_wait(f'{imc}\nClassificação: Sobrepeso')
                elif imc > 30.0 and imc < 39.9:
                    sg.popup_no_wait(f'{imc}\nClassificação: Obesidade')
                elif imc > 40.0:
                    sg.popup_no_wait(f'{imc}\nClassificação: Obesidade Grave')
                else:
                    print('algo de errado não está certo')       
Start = Imc()
Start.Iniciar()