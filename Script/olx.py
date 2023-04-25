from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase
import pyautogui


navegador = webdriver.Chrome()

navegador.get('https://www2.olx.com.br/ai/form/0/')

pyautogui.sleep(5)

##Usuario
navegador.find_element(By.XPATH, '//*[@id="input-1"]').send_keys('coloque seu usuario')

pyautogui.sleep(1)

#Senha
navegador.find_element(By.XPATH, '//*[@id="password-input"]').send_keys('Coloque sua senha')

navegador.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div[1]/div[2]/form/button').click()

pyautogui.sleep(5)

#Seleciona a Categoria via Xpath
navegador.find_element(By.XPATH, '//*[@id="root"]/div[3]/form/div/div/section/ul/li[3]').click()

pyautogui.sleep(1)

#Sub categoria
navegador.find_element(By.XPATH, '//*[@id="category_item-5080"]').click()

#Arquivo no mesmo diretorio Titulo
with open("Cabecalho.txt", "r", encoding='utf8') as arquivo:
    Cabecalho = arquivo.read()
    print(Cabecalho)

pyautogui.sleep(1)

navegador.find_element(By.XPATH, '//*[@id="subject"]').send_keys(Cabecalho)

#Arquivo no mesmo diretorio Descrisão
with open("Corpo.txt", "r", encoding='utf8') as arquivo:
    Corpo = arquivo.read()
    print(Corpo)

navegador.find_element(By.XPATH, '//*[@id="body"]').send_keys(Corpo)

pyautogui.sleep(1)

navegador.find_element(By.XPATH,'//*[@id="condition"]').send_keys('Novo')

pyautogui.sleep(1)

#Valor do produto
navegador.find_element(By.XPATH, '//*[@id="price"]').send_keys('1')


#Obs... Caminho da Img do post pode adicionar mais de 1 so capiar e colar
navegador.find_element(By.XPATH, '//*[@id="group-image-container"]/div[2]/div[2]/input').send_keys("C:/Users/Paulo/Desktop/Script/photos/3.png")

#CEP
navegador.find_element(By.XPATH, '//*[@id="zipcode"]').send_keys('')

#aqui ficaria a api de resolver

pyautogui.sleep(1000)
