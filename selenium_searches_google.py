# from main_test import SendText

from selenium import webdriver
from selenium.webdriver.common.by import By

open_file = open("texto_arquivado.txt", "r+")
texto= open_file.read()
ja_lido = texto
def searches_google(text_searches_google):
                driver = webdriver.Chrome()

                driver.get("https://www.google.com")

                title = driver.title
                assert title == "Web form"

                driver.implicitly_wait(0.5)

                text_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
                submit_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")

                text_box.send_keys(text_searches_google)
                submit_button.click()

                message = driver.find_element(by=By.ID, value="message")
                value = message.text
                assert value == "Received!"

               #  driver.quit()


if texto != "" : 
   searches_google(texto) 
   
   open_file.close()
   if open_file.close():
      print("selenium_searches fechou o file")

else:
   print("Nada escrito")
