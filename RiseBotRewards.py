import threading
import time
import pyautogui
import os
import keyboard
import random

py = pyautogui
numero_aleatorio = random.randint(1, 9999999)

def confirm():
    resposta = py.confirm(text='Start Bot --Version 4.5?', buttons=['Yes', 'No'])
    if resposta == 'Yes':
        return True
    else:
        return False

if confirm():
    py.alert('The Bot will start, remember to pause the bot press the "   Q   " key repeatedly until the automation stops | O bot será iniciado, lembre-se que para pausar o bot aperte a tecla "   Q   " repetidas vezes até que a automação pare.')
    time.sleep(0.3)
    py.hotkey('winleft','r')
    time.sleep(0.3)
    py.write('msedge')
    time.sleep(0.3)
    py.press('enter')
    time.sleep(2)
    py.press('f4')
    time.sleep(1)
    py.typewrite('https://rewards.bing.com/redeem/pointsbreakdown')
    time.sleep(0.5)
    py.press('enter')
    py.hotkey('ctrl','t')
    pyautogui.typewrite(str(numero_aleatorio))
    py.press('enter')
    py.hotkey('ctrl','w')

    def x():
        for _ in range(37):
            numero_aleatorio = random.randint(1, 9999999)
            py.hotkey('ctrl','t')
            pyautogui.typewrite(str(numero_aleatorio))
            py.press('enter')
            py.hotkey('ctrl','w')

    def y(): ## Tranca ao apertar q
        while True:
            if keyboard.is_pressed('q'): 
                os._exit(0)

    threading.Thread(target=y).start() ## Roda duas funções ao mesmo tempo      
    threading.Thread(target=x).start() ## Roda duas funções ao mesmo tempo
