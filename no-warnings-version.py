import threading
import time
import pyautogui
import os
import keyboard
import random

py = pyautogui
numero_aleatorio = random.randint(1, 9999999)

py.hotkey('winleft','r')
py.write('msedge')
py.press('enter')
time.sleep(0.5)
py.typewrite('https://rewards.bing.com/redeem/pointsbreakdown')
py.press('enter')
py.hotkey('ctrl','t')
pyautogui.typewrite(str(numero_aleatorio))
py.press('enter')
py.hotkey('ctrl','w')

def x():
    while True:

        numero_aleatorio = random.randint(1, 9999999)
        py.hotkey('ctrl','t')
        pyautogui.typewrite(str(numero_aleatorio))
        py.press('enter')
        py.hotkey('ctrl','w')
        py.press('f5')  

def y(): ## Tranca ao aperta q
    while True:
        if keyboard.is_pressed('q'): 
            os._exit(0)



threading.Thread(target=y).start() ## Roda duas funções ao mesmo tempo      
threading.Thread(target=x).start() ## Roda duas funções ao mesmo tempo
