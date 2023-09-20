import speech_recognition as sr
import re

import pyttsx3

nome = 'Rafael'


while (True):
    nome = 'Rafael'
    mic = sr.Recognizer()
    with sr.Microphone() as  source:
        engine = pyttsx3.init()
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")
        mic.adjust_for_ambient_noise(source)
        
        print('vamos começar, fale algo...')
        
        audio = mic.listen(source)
        
        try:
            frase = mic.recognize_google(audio,language='pt-BR')
            print('voce falou:  '+ frase)
            if (re.search(r'\b' + 'ajudar' + r'\b',format(frase))):
                engine.say("Ajuda")
                engine.runAndWait()
                print('algo relacionado a ajuda.')
            elif (re.search(r'\b' + 'Qual é o meu nome' + r'\b',format(frase))):
                engine.say('seu nome é Rafael')
                engine.runAndWait()
            elif (re.search(r'\b' + 'Qual é o seu nome' + r'\b',format(frase))):
                engine.say('meu nome é assistente de big dog')
                engine.runAndWait()
            elif (re.search(r'\b' + 'pare' + r'\b',format(frase))):
                engine.say("Até logo")
                engine.runAndWait()
                break 
        except sr.UnknownValueError:
            print('ops, algo deu errado')