import pyautogui
import time

def click(): 
    time.sleep(0.5)     
    pyautogui.click()

def main():
    for i in range(10):#you can set how much times you have to click in range(no. of times to click) 
        click()

main()
