#Passo 1: entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui as pa
import time

pa.PAUSE = 1
#abrir o navegador
pa.hotkey("win", "s")
pa.write("chrome")
pa.press("enter")
time.sleep(3) #pausa de espera nessa linha

#entrar no link
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press("enter")
time.sleep(3)
#Passo 2: Login
pa.click(x=621, y=390)
pa.write("pythonimpressionador@gmail.com")
pa.press("tab")
pa.write("1234")
pa.press("enter")
time.sleep(3)

#Passo 3: importar a base de produtos para cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)
#Passo 4: cadastrar um produto
#Passo 5: repetir o processo de cadastro até o fim