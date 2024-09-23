# passo a passo do projeto 

# 1. Abrir o sistema da empresa
   
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

#import time pausa o tempo, para no lugar que você quer!


pyautogui.PAUSE = 0.5

#pyautogui.click (clicar com o mouse)
#pyautogui.write (escrever um texto)  
#pyautogui.press (pressionar uma tecla do teclado)
#pyautogui.hotkey (apertar um conjunto de teclas)
#pyautogui.pause (pausar o tempo nescessario)
#print(pyautogui.position()) (indica a posição de onde seu mouse estiver apontando!)

#abrir o navegador (firefox)
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")


# entrar no site do sistemda
pyautogui.click(x=587, y=58)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# vou usar o time.sleep pra congelar um pouco, para o comando não atropelar o outro
time.sleep(2)

# 2. Fazer Login

pyautogui.click(x=780, y=405)
pyautogui.write("eutestando@gmail.com")
pyautogui.press("tab")
pyautogui.write("italolobo10")
pyautogui.press("enter")

# 3. Abrir/importar a base de dados de produtos para cadastrar
import pandas as pd

tabela =  pd.read_csv("produtos.csv")

print(tabela)


# 4. Cadastrar um produto

for linha in tabela.index:


    codigo = (str(tabela.loc[linha, "codigo"]))


    #clicar no campo do código do produto 
    pyautogui.click(x=869, y=281)

    #preencher o campo com o código
    pyautogui.write(codigo)

    #passar para linha de baixo
    pyautogui.press("tab")


    #marca
    pyautogui.write (str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #tipo 
    pyautogui.write (str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #categoria
    pyautogui.write (str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preço_unitario
    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo 
    pyautogui.write (str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
         pyautogui.write (obs)

    pyautogui.press("tab")
    
    pyautogui.press("enter")
    #pyautogui.scroll(50000
    
    # scroll negativo desce a tela, scroll positivo sobe a tela!


# 5. Repetir isso tudo até acabar a lista de produtos





