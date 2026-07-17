import pyautogui
from time import sleep
pyautogui.keyDown("win")
pyautogui.press("r")
pyautogui.keyUp("win")
pyautogui.write("firefox")
pyautogui.press("enter")
sleep(2)
pyautogui.write("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
pyautogui.press("enter")
sleep(2)
pyautogui.press("space")
