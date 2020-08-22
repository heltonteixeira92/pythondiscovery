import PySimpleGUI as sg

class Calculadora:
    def __init__(self):
        pass

    def Inicio(self):
        #layout
        layout = [
            [sg.Text('CALCULADORA')],
            [sg.Input( key = 'input')],
            [sg.Button('1'),sg.Button('2'),sg.Button('3')],
            [sg.Button('4'),sg.Button('5'),sg.Button('6')],
            [sg.Button('7'),sg.Button('8'),sg.Button('9')],
            [sg.Button('Submit'),sg.Button('0'),sg.Button('Clear', bind_return_key=True)]
        ]
  
        #janela
        window = sg.Window('Calculadora', layout, default_button_element_size=(5,2))
        keys_entered = ''

        while True:
            event, values = window.Read()
            if event == 'Submit':
                keys_entered = values['input']
                window['output'].update(keys_entered)
            if event =='Exit':
                break


start = Calculadora()
start.Inicio()



                
                

        #extrair dados
        #fazer algo

