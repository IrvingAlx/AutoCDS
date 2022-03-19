from PIL import Image
import pyautogui


pyautogui.hotkey("win")
pyautogui.sleep(2)
pyautogui.typewrite("chrome")
pyautogui.hotkey("enter")
pyautogui.sleep(5)
pyautogui.typewrite("https://cuestionariodesalud.ibero.mx/#/login")
pyautogui.hotkey("enter")

pyautogui.sleep(3)

pyautogui.hotkey("f5")

pyautogui.sleep(1)

xyhw = pyautogui.locateOnScreen("conver2ted.png")
print(xyhw)
xyhw = pyautogui.center(xyhw)

pyautogui.click(xyhw)

pyautogui.sleep(2)

for pos in pyautogui.locateAllOnScreen("conver3ted.png"):
   print(pos)
   pyautogui.click(pos)

xyhw = pyautogui.locateOnScreen("conver4ted.png")
xyhw = pyautogui.center(xyhw)

pyautogui.click(xyhw)
