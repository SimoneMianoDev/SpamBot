import time
import pyperclip
import pyautogui

time.sleep(5)


x=0

while x <= 9999:
    x = x + 1
    f = open("Text", "r")
    for char in f:
        pyperclip.copy(char)
        pyautogui.hotkey('ctrl', 'v', interval=0.001)
        pyautogui.typewrite("\n")





