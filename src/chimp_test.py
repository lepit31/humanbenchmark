import pyautogui
import time

max_btn = 40

def clickBtn():
    btns = []
    for i in range(0, max_btn):
        btn = pyautogui.locateOnScreen(f"./ressources/{i+1}.png")
        if btn is not None:
            btns.append(btn)

    print(f" nb btns {len(btns)} ")
    for btn in btns:
        pyautogui.click(btn)



try:
    while True :
        clickBtn()
        #time.sleep(1)
        btn_continue =pyautogui.locateOnScreen("./ressources/continue.png")
        pyautogui.click(btn_continue)
except KeyboardInterrupt:
    print("Monitoring stopped by user.")