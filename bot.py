import pyautogui
from time import sleep

limite_msg = input('Numero de msg: ')
msg = input('mensagem: ')

i = 0
sleep(4)

while i < int(limite_msg):
    pyautogui.typewrite(limite_msg)
    pyautogui.press('Enter')
    i+=1