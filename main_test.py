# import argparse
# import queue
# import sys
# import sounddevice as sd
import json
import core

# from test import oi

from vosk import Model, KaldiRecognizer

import sys
import os
import subprocess
from subprocess import Popen, PIPE

import pyttsx3
import pyaudio 
import pyautogui
# from pydub import AudioSegment
# from pydub.playback import play
# import pyperclip
import time



from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import webbrowser

from multiprocessing import Process, Queue

from test import oi

# from selenium_searches_google import searches_google
# import selenium_searches_google

ordens = 'abra', 'abrir', 'pesquise', 'veja', 'responda', 'novo', 'lá',
# a

pronomes = 'quem', 
# b

adverbios = 'onde', 
# c

verbos = 'é', 'fica', 'são',
# d


wake_words = 'lá',

smartin = False
def smartin_window(smartin):
   if smartin == True:
      os.chdir('D:\Projects\Personal\Projects\MANU(0.0)\APPs\SmartinWindow')
      os.system("python main.py")
      smartin == False

dicio = { 'terminal' : r'cmd.exe',
          'hotel' : r'C:\Users\Paulo Alex\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\GitHub, Inc\GitHubDesktop.exe',
          'caixa de entrada': 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox',
          'mensagens' : 'https://web.whatsapp.com/',
          'projecto' : r'D:\PycharmProjects\pythonProject2\main.exe',
          'projeto' : r'D:\PycharmProjects\pythonProject2\main.exe',
          'código' : r'python.exe',
          'janelas' : True
         }


# def searches_google(text_searches_google):
#                 driver = webdriver.Chrome()

#                 driver.get("https://www.google.com")

#                 title = driver.title
#                 # assert title == "Web form"

#                 driver.implicitly_wait(0.5)

#                 text_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
#                 submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")

#                 text_box.send_keys(text_searches_google)
#                 submit_button.click()

#                 message = driver.find_element(by=By.ID, value="message")
#                 value = message.text
#                 assert value == "Received!"

#                 driver.quit()


codigo_tipo_acao = []

list_text_equals_database = []
# igual ao list_text, mas sem os substantivos. Palavras de "text" iguais ao banco de dados.




list_ordens = list(ordens)
list_pronomes = list(pronomes)
list_adverbios = list(adverbios)
list_verbos = list(verbos)

text_search = ''

# os.startfile(r'C:\Users\Suporte\AppData\Local\Google\Chrome\Application\chrome.exe')


#Automação Web
# navegador = webdriver.Chrome("Paulo -0 Chrome")

# navegador.get("https://docs.google.com/document/u/0/")

#Síntese de fala
engine = pyttsx3.init()


def speak(text):

   engine.say(text)
   engine.runAndWait()

#reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)

stream.start_stream()
#presta atenção no buffer, se der erro usa buffer=2048




def restart_program():
   os.chdir('C:')
   python = sys.executable
   os.execl(python, python, * sys.argv)
   
   # try this
#    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')
#    subprocess.call([sys.executable, os.path.realpath(__file__)] +
# sys.argv[1:])

def timer(five):
   five = 0
   time.sleep(5)
   five = 5
   return five

def counter(search):
   five_secs = time.time() + int(10)
   while time.time() <  five_secs:
      if search != "olá":
         print("ok")
         # answer = searches_google(s = text)
      return search
   
def send_text(content):
   if content != "lá":
     content = text
     return content

#Loop do reconhecimento de fala
number = 0 
TF = False
time_online = False

while True:
    data = stream.read(8196)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
      #   cpu_usage = os.system('wmic cpu get loadpercentage')
        if result is not None:
             text = result['text']
             print(text)
            #  print("ç")
            #  speak(text)
             
#se index >= 0, então a pergunta é verdadeira(existe) e 0++ é posição


             if text.find('horas') >= 0 and (text.find('são') >= 0 or text.find('diga') >= 0):
                speak(core.SystemInfo.get_time())

             if text.find('tudo') >= 0 and (text.find('encerra') >= 0 or text.find('desliga') >= 0):
                b = speak('Até mais chefe')
                exit()
                

             if text.find('tudo') >=0 and (text.find('reinicia') >= 0 or text.find('recomeça') >= 0):
                restart_program()

            
             if text.find('caixa de entrada') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
            
                os.startfile('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox') 

             if text.find('tradutor') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
            
                os.startfile('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate') 
               #  webbrowser.open('https://web.whatsapp.com/', new = 0, autoraise = False)          
               
             if text.find('isso') >=0 and (text.find('traduza') >= 0 or text.find('traduz') >= 0):
                pyautogui.keyDown('ctrl')
                pyautogui.press('c')
                pyautogui.keyUp('ctrl')
                time.sleep(3)
                os.startfile('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate')  
                time.sleep(3)
                pyautogui.keyDown('ctrl')
                pyautogui.press('v')
                pyautogui.keyUp('ctrl')
             
             
             print("before",time_online)
             if text.find('internet') >= 0 and text.find('horas') >= 0:
                time_online = True
                print("after",time_online)
                if time_online == True:
                    os.startfile(r"D:\PycharmProjects\pythonProject4\main.exe")
                    print("inside",time_online)
                    
             oi(text)
             gracias = 'bom dia','boa tarde','boa noite','vamos trabalhar'
             
            #  if text.find('projeto') >=0 and (text.find('novo') >= 0 or text.find('cria') >= 0):
            



            
            #     os.startfile(r'D:\PycharmProjects\pythonProject2\main.exe') 

             for i in gracias:
                 
              if text == i:
                 speak('Olá senhor Paulo, como vai?')
           
             

             list_text = text.split(' ')
             #  list_text transforma todo text em lista             
           

                
             detect_list_ordens = []
             for a in list_ordens:
                for aa in list_text:
                  if aa == a:
                    
                    
                    a1 = codigo_tipo_acao.append('a')
                    list_text_equals_database.append(a)
                  

             detect_list_pronomes = []
             for b in list_pronomes:
                for bb in list_text:
                  if bb == b:
                  #   detect_list_pronomes = b
                    
                    b1 = codigo_tipo_acao.append('b')
                    list_text_equals_database.append(b)
                 

             detect_list_adverbios = []     
             for c in list_adverbios:
                for cc in list_text:
                  if cc == c:
                  #   detect_list_adverbios = c
                    
                    c1 = codigo_tipo_acao.append('c')
                    list_text_equals_database.append(c)
                  
             
             detect_list_verbos = []
             for d in list_verbos:
                for dd in list_text:
                  if dd == d:
                  #   detect_list_verbos = d
                  
                    d1 = codigo_tipo_acao.append('d')
                    list_text_equals_database.append(d)
                  
                  
               
            #  print(list_text)
            #  print(list_text_equals_database)

             for _ in list_text_equals_database:
                if _ in list_text:
                  list_text.remove(_)
                    
             list_substantivo = list_text
             # agora sobra apenas os substantivos de list_texts
             # print(list_substantivo)

             for icb in list_substantivo:
                if icb != '':
                   if 'z' not in codigo_tipo_acao:
                      codigo_tipo_acao.append('z')
             # Para cada elemento de list_substantivo se for diferente de vazio e 'z' não está em codigo_tipo_acao, 
             # append 'z' em codigo_tipo_acao  
             


             if codigo_tipo_acao == ['a','z']:
               try: 
                 dicio[''.join(list_substantivo)]                 
               except:
                    print("Deu erro")
                    pass
               else:
                 try:
                    
                    os.startfile(dicio[''.join(list_substantivo)]) 

                    
                 except:
                    print("Deu erro 2")
                  #   pass
                    smartin_window(dicio[''.join(list_substantivo)])
               #   else:

             elif (codigo_tipo_acao != [] and text == "lá") or TF == True:
               print(text , " OUVINDO PESQUISA")

               TF = True

               if TF == True:
                  # print(TF)
                  number += 1
                  # print(number)
                  # print("ouvindo por 5s")

                  if text != "lá" and text != '':
                  #   print(text)
                    print("PESQUISANDO")
                    speak("Pesquisando")
                    
                    p = open("texto_arquivado.txt", "a")
                    p.write(text)
                    if p:
                       print("File is opened")

                  #   result = subprocess.run(["python", "selenium_searches_google.py"], capture_output=True, text=True)
                  #   if result == True:
                        # print("Result is true")
                        
                    p.close()
                    if p.close :
                       print("File is closed")
                    
                    result = subprocess.run(["python", "selenium_searches_google.py"], capture_output=True, text=True)
                    
                    apagar_texto = open("texto_arquivado.txt", "a")
                    apagar_texto.truncate(0)
                    apagar_texto.close()

                  #   print(type(text))
                 
                  
               if number == 5:
                  number = 0
                  print("zerou")
                
                  TF = False
                  # print(TF)
                 
 
             print(codigo_tipo_acao)

             list_text_equals_database = []     
             codigo_tipo_acao = []
             


