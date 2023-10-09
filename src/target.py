import pyautogui

while True :
    target =pyautogui.locateOnScreen("./ressources/target.png", confidence=0.6)
    print(target)
    if target is not None:
        pyautogui.click(target)