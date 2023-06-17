# import argparse
# import queue
# import sys
# import sounddevice as sd
import json
import core

from vosk import Model, KaldiRecognizer

import sys
import os



import pyttsx3
import pyaudio 
# import pyautogui
# from pydub import AudioSegment
# from pydub.playback import play
# import pyperclip
import time



from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import webbrowser


ord = 'abra', 'pesquise', 'veja', 'responda',
# a

prn = 'quem', 
# b

adv = 'onde', 
# c

vrb = 'é', 'fica', 'são',
# d

dicio = { 'terminal' : 'cmd.exe',
          'hotel' : r'C:\Users\Suporte\AppData\Local\GitHubDesktop\GitHubDesktop.exe',
          'caixa de entrada': 'https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox',
          'mensagens' : 'https://web.whatsapp.com/',
          
         }


resulted = []

# text = 'onde fica o rochedo de gibraltar'


lOrd = list(ord)
lPrn = list(prn)
lAdv = list(adv)
lVrb = list(vrb)

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
   python = sys.executable
   os.execl(python, python, * sys.argv)


#Loop do reconhecimento de fala
while True:
    data = stream.read(8196)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)
        
        
        if result is not None:
             text = result['text']
             print(text)
            #  speak(text)
            
            


#se index >= 0, então a pergunta é verdadeira(existe) e 0++ é posição


             if text.find('horas') >= 0 and (text.find('são') >= 0 or text.find('diga') >= 0):
                speak(core.SystemInfo.get_time())

             if text.find('tudo') >= 0 and (text.find('encerra') >= 0 or text.find('desliga') >= 0):
                b = speak('Até mais chefe')
                exit()
             
            #  if text.find('som') >= 0 and (text.find('liga') >= 0 or text.find('desliga') >= 0):
            #     pyautogui.hotkey('f5', 'fn')
                

             if text.find('tudo') >=0 and (text.find('reinicia') >= 0 or text.find('recomeça') >= 0):
                restart_program()
             
            #  if text.find('terminal') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
            #     os.startfile('cmd.exe')
               #  sound = AudioSegment.from_file(r'manu\\door-open.wav')
               #  play(sound)
             
            #  if text.find('hotel') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
                
            #     speak('processando isso')
            #     os.startfile(r'C:\Users\Suporte\AppData\Local\GitHubDesktop\GitHubDesktop.exe')
            
            #  if text.find('caixa de entrada') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
            
            #     os.startfile('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox') 

             if text.find('tradutor') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
            
               #  os.startfile('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate') 
                webbrowser.open('https://web.whatsapp.com/', new = 0, autoraise = False)          
               
            #  if text.find('isso') >=0 and (text.find('traduza') >= 0 or text.find('traduz') >= 0):
            #     pyautogui.keyDown('ctrl')
            #     pyautogui.press('c')
            #     pyautogui.keyUp('ctrl')
            #     time.sleep(3)
            #     os.startfile('https://translate.google.com.br/?hl=pt-BR&sl=en&tl=pt&op=translate')  
            #     time.sleep(3)
            #     pyautogui.keyDown('ctrl')
            #     pyautogui.press('v')
            #     pyautogui.keyUp('ctrl')

             gracias = 'bom dia','boa tarde','boa noite','vamos trabalhar'

             for i in gracias:
                 
              if text == i:
                 speak('Olá senhor Paulo, como vai?')
            #problema/bug: caso alguém fale, 'tudo encerrado'. Pode não estar se referindo à manu.
            #o ideal seria ter o termo manu adicionando probabilidade ao reconhecimento, além de
            #caixa de pergunta para confirmação da ordem.

            #  if text.find('agora') >= 0:
               #  navegador = webdriver.Chrome()
               #  print(str(navegador.current_url))
               #  http_host = request.META.get('HTTP_HOST')

             lText = text.split(' ')
             
             
                

             for a in lOrd:
                for aa in lText:
                  if aa == a:
                    txA = a
                    
                    a1 = resulted.append('a')
                    
                  
             for b in lPrn:
                for bb in lText:
                  if bb == b:
                    txB = b
                    
                    b1 = resulted.append('b')

                  
             for c in lAdv:
                for cc in lText:
                  if cc == c:
                    txC = c
                    
                    c1 = resulted.append('c')
                  
                
             for d in lVrb:
                for dd in lText:
                  if dd == d:
                    txD = d
                  
                    d1 = resulted.append('d')
                  
                  
                  
             txT = []


             try: txA
             except NameError: 
                pass
             else: 
                txT.append(txA)


             try: txB
             except NameError: 
                pass
             else: 
                txT.append(txB)


             try: txC
             except NameError: 
                pass
             else: 
                txT.append(txC)


             try: txD
             except NameError: 
                pass
             else: 
                txT.append(txD)



            #  if aa == a:
            #     True
            #  elif bb == b:
            #     True
            #  elif cc == c: 
            #     True
            #  elif dd == d:
            #     True
            #  elif dd == d:
            #     True
            #  else:

                  # resulted.append('z') 
              


             subst = []

             for _ in txT:
                if _ in lText:
                  lText.remove(_)
                  # resulted.append('z') 
             print(lText)

             for icb in lText:
                if icb != '':
                   if 'z' not in resulted:
                      resulted.append('z')

               #  if icb != '':
               #     resulted.append('z')
               #     if len(icb) >= 2:
               #       resulted.remove('z')

             def test_eight_components(s):
                  driver = webdriver.Chrome()

                  driver.get("https://www.google.com")

                  title = driver.title
                  # assert title == "Web form"

                  driver.implicitly_wait(0.5)

                  text_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
                  submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")

                  text_box.send_keys(s)
                  submit_button.click()

                  message = driver.find_element(by=By.ID, value="message")
                  value = message.text
                  assert value == "Received!"

                  driver.quit()
 
            #  mL = ' '.join(lText)
            #  print(mL)
             print(resulted)
            #  print(' '.join(subst))
            #  ltSb = ' '.join(subst)
            #  resulted = []
            #  print(ltSb)
            #  if ltSb != ' ':
            #     print('Ele existe!')
            #  oF = 'onde fica '
            #  sb = ['terminal',]
            #  print(dicio[' '.join(sb)])
            #  if resulted == ['c', 'd', 'z' ]:
  
            #   answer = test_eight_components(s = mL, j = oF)
 

             fiveSecs = time.time() + 5
             zeroSecs = time.time()

             if resulted == ['a','z']:
               try: 
                 dicio[''.join(lText)]                 
               except:
                 print("Deu erro")

                 pass
               else:
                 os.startfile(dicio[''.join(lText)])  

             elif resulted != [] and text.find("olá") >= 0:
               while zeroSecs < fiveSecs:
                  print("É pesquisa!")
                  answer = test_eight_components(s = text)
                  break
             resulted = []

             
            #  else:

            #    test_eight_components(s = text)


# dt = dicio['terminal']

# print(dt)
