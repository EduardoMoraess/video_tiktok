import pyautogui as spam
from time import sleep

# Solicita o número de mensagens e a mensagem a ser enviada
limite_msg = input('Numero de mensagens:=>')
msg = input('Digite sua mensagem:=>')

i = 0
sleep(4)  # Aguarda 4 segundos antes de começar

# Loop para enviar as mensagens
while i < int(limite_msg):
    spam.typewrite(msg)
    spam.press('Enter')
    i += 1  # Incrementa o contador para evitar loop infinito