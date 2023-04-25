
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
import pyautogui
from pydub import AudioSegment
from pydub.playback import play
import pyperclip
import time


from selenium import webdriver

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
            
            #  if text == 'que horas são' or text == 'me diga as horas':
            #     speak(core.SystemInfo.get_time())


#se index >= 0, então a pergunta é verdadeira(existe) e 0++ é posição


             if text.find('horas') >= 0 and (text.find('são') >= 0 or text.find('diga') >= 0):
                speak(core.SystemInfo.get_time())
            #problema/bug: caso alguém fale, 'tudo encerrado'. Pode não estar se referindo à manu.
            #o ideal seria ter o termo manu adicionando probabilidade ao reconhecimento, além de
            #caixa de pergunta para confirmação da ordem.

# words = text.split(' ')

# if words.index('horas') >= 0 and (words.index('são') >= 0 or words.index('diga') >= 0): 
   
             if text.find('tudo') >= 0 and (text.find('encerra') >= 0 or text.find('desliga') >= 0):
                b = speak('Até mais chefe')
                exit()
             
             if text.find('som') >= 0 and (text.find('liga') >= 0 or text.find('desliga') >= 0):
                pyautogui.hotkey('f5', 'fn')
                

             if text.find('tudo') >=0 and (text.find('reinicia') >= 0 or text.find('recomeça') >= 0):
                restart_program()
             
             if text.find('terminal') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
                os.startfile('cmd.exe')
               #  sound = AudioSegment.from_mp3("manu\\door-open.wav")
               #  play(sound)
             
             if text.find('hotel') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
                os.startfile(r'C:\Users\Suporte\AppData\Local\GitHubDesktop\GitHubDesktop.exe')
            
             if text.find('caixa de entrada') >=0 and (text.find('abra') >= 0 or text.find('roda') >= 0):
                os.startfile('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')            
               

             gracias = 'bom dia','boa tarde','boa noite','vamos trabalhar'

             for i in gracias:
                 
              if text == i:
                 speak('Olá senhor Paulo, como vai?')
                 

            #  if text == "terminal":
            #      f = open('__init__.py', 'r')
            #      print(f.read())

#DETECTA SAUDAÇÃO
#  saudacao = 'bom dia, boa tarde, boa noite'
#  if text == saudacao:
   
               
               

#DECIDE SAUDAÇÃO DE ACORDO HORAS
# if core.SystemInfo.get_time() >= 6:
#      speak('bom dia')
# if core.SystemInfo.get_time() >= 13 or <= 18 :
#    speak('bom dia')

# if core.SystemInfo.get_time() >= 6:
#    speak('bom dia')

# COMANDOS PYAUTOGUI
#  if text == 'som' or text == 'Abrir Google Documentos':
#     pyautogui.PAUSE = 1
#     pyautogui.hotkey("fn", "f4")  
               
#  pyautogui.hotkey("ctrl", "t")
#  pyperclip.copy("https://docs.google.com/document/u/0/")
#  pyautogui.hotkey("ctrl", "v")
#  pyautogui.press("enter")
#  time.sleep(5)

#  pyautogui.write("https://docs.google.com/document/u/0/")
#  pyautogui.press("enter")
#  pyperclip.copy("https://docs.google.com/document/u/0/")
#  pyautogui.hotkey("ctrl", "f")
#  time.sleep(5)


             

            #  if text == 'som':
            #     py.PAUSE = 2
            #     py.press("win")
            #     py.press("tab")
            #    #  py.press("keyboard")   
            #     py.press("down")

            #  if text == 'musica':
            #     py.PAUSE = 1
            #     py.press("win")
            #     py.write("chrome")
            #     py.press("enter")
            #     pyperclip.copy("https://docs.google.com/document/u/0/")
            #     py.hotkey("ctrl", "v")
            #     time.sleep(5)

        #   if text: 'VAriáveis S igual a 2 e T igual a 1'
                            
        # print('Lâmpada ligada senhor Paulo')
        # speak('Captei, e devo colocar em qual equação? Do sorvete?')

        #   if text : 'Desligue computador'
        #       exit()
    
        #   else:
        #      os.system ("shutdonw /s /t 1")


        
# q = queue.Queue()

# def int_or_str(text):
#     """Helper function for argument parsing."""
#     try:
#         return int(text)
#     except ValueError:
#         return text

# def callback(indata, frames, time, status):
#     """This is called (from a separate thread) for each audio block."""
#     if status:
#         print(status, file=sys.stderr)
#     q.put(bytes(indata))

# parser = argparse.ArgumentParser(add_help=False)
# parser.add_argument(
#     "-l", "--list-devices", action="store_true",
#     help="show list of audio devices and exit")
# args, remaining = parser.parse_known_args()
# if args.list_devices:
#     print(sd.query_devices())
#     parser.exit(0)
# parser = argparse.ArgumentParser(
#     description=__doc__,
#     formatter_class=argparse.RawDescriptionHelpFormatter,
#     parents=[parser])
# parser.add_argument(
#     "-f", "--filename", type=str, metavar="FILENAME",
#     help="audio file to store recording to")
# parser.add_argument(
#     "-d", "--device", type=int_or_str,
#     help="input device (numeric ID or substring)")
# parser.add_argument(
#     "-r", "--samplerate", type=int, help="sampling rate")
# parser.add_argument(
#     "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
# args = parser.parse_args(remaining)

# try:
#     if args.samplerate is None:
#         device_info = sd.query_devices(args.device, "input")
#         # soundfile expects an int, sounddevice provides a float:
#         args.samplerate = int(device_info["default_samplerate"])
        
#     if args.model is None:
#         model = Model(lang="pt")
#     else:
#         model = Model(lang=args.model)

#     if args.filename:
#         dump_fn = open(args.filename, "wb")
#     else:
#         dump_fn = None

#     with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
#             dtype="int16", channels=1, callback=callback):
#         print("#" * 80)
#         print("Press Ctrl+C to stop the recording")
#         print("#" * 80)

#         rec = KaldiRecognizer(model, args.samplerate)
#         while True:
#             data = q.get()
#             if rec.AcceptWaveform(data):
#                 result = rec.Result()
#                 result = json.loads(result)
#             # else:
#             #     print(rec.PartialResult())
#             # if dump_fn is not None:
#             #     dump_fn.write(data)

#                 if result is not None:
#                     text = result['text']
#                     print(text)
#                     speak(text)

# except KeyboardInterrupt:
#     print("\nDone")
#     parser.exit(0)
# except Exception as e:
#     parser.exit(type(e).__name__ + ": " + str(e))