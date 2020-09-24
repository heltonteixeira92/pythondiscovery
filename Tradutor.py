#tradutor usando a API google translator

from googletrans import Translator

frase = '''hello my little friend'''

# Creating an instance of Translator to use
# Google Translate ajax API
translator = Translator()

#dectec- auto detects language of the input text
dt = translator.detect(frase)
print(dt)

#translate()-traslates the text from source language
#to destination language
#translate(self, text, dest='en', src='auto')
translated = translator.translate(frase, dest ='pt')

print(translated.text)

