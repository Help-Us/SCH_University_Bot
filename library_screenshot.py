#https://code.i-harness.com/ko/q/120718
import pyscreenshot as ImageGrab
#from selenium import webdriver
import pyautogui
import time

#browser = webdriver.Chrome()
#browser.get('https://eseat.sch.ac.kr/EZ5500/SEAT/RoomDisplay.aspx?mode=display')
a=True
time.sleep(4)
while a:
    time.sleep(10)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    time.sleep(3)
    img = ImageGrab.grab(bbox=(382, 424, 1442, 926))
    #제 1 열람실
    img.save("/var/www/html/photo/first.png")
    time.sleep(1)
    pyautogui.click(505,318)
    time.sleep(2)
    #제 2 열람실
    img = ImageGrab.grab(bbox=(380, 455, 1439, 913))
    img.save("/var/www/html/photo/second.png")
    time.sleep(1)
    pyautogui.click(606,362)
    time.sleep(1)
    #제 3 열람실
    img = ImageGrab.grab(bbox=(380, 511, 1433, 917))
    img.save("/var/www/html/photo/third.png")
    time.sleep(1)
    pyautogui.click(720,428)
    time.sleep(1)
    #멀티존
    img = ImageGrab.grab(bbox=(646, 562, 1211, 844))
    img.save("/var/www/html/photo/multi.png")
    time.sleep(1)
    pyautogui.click(841,447)
    time.sleep(1)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    pyautogui.click(1815,953)
    time.sleep(2)
    #인터넷존
    img = ImageGrab.grab(bbox=(833, 477, 1001, 913))
    img.save("/var/www/html/photo/internet.png")
    pyautogui.click(946,394)
    time.sleep(2)
    #프리미어
    img = ImageGrab.grab(bbox=(784, 569, 1078, 850))
    img.save("/var/www/html/photo/pre.png")
    pyautogui.click(80,117)

