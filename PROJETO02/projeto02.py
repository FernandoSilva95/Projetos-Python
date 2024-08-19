import pyautogui
import pyperclip    
import webbrowser
import time

import yfinance

ticker = input("Digite o código da ação desejada: ")

dados = yfinance.Ticker(ticker).history(start="2023-01-01", end="2023-12-31")
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

destinatario = "antonnyfernando@gmail.com"
assunto = "Análises do Projeto 2023"

mensagem = f"""
Prezados,

Segue as análises do projeto {ticker}: 

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

At.te,
Fernando Silva.

"""

# abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando a pausa de 3 segundos
pyautogui.PAUSE = 3

# clicar no botão escrever
pyautogui.click(x=79, y=185)

# digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do e-mail e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar
pyautogui.click(x=840, y=697)

# fechar o gmail
pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso")