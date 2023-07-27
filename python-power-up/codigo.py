#Passo 1: entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login


import pyautogui as pa
import time

pa.PAUSE = 2
#abrir o navegador
pa.hotkey("win", "s")
pa.write("chrome")
pa.press("enter")
time.sleep(3)
#pausa de espera nessa linha

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

#clicar no campo do código
for linha in tabela.index:
    pa.click(x=550, y=273)
    #pegar da tabela o valor do campo que deseja preencher
    #preencher o campo
    pa.write(str(tabela.loc[linha, "codigo"]))  
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "marca"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "tipo"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "categoria"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "preco_unitario"]))
    pa.press("tab")
    pa.write(str(tabela.loc[linha, "custo"]))
    pa.press("tab")
    if not pd.isna(tabela.loc[linha, "obs"]):
        pa.write(str(tabela.loc[linha, "obs"]))
    pa.press("tab")
    pa.press("enter")
    pa.press("home")
#Passo 5: repetir o processo de cadastro até o fim