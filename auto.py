import pyautogui as p
import time
import threading as th

timer = 60
p.click(x=30,y=83)

def start_timer():
    global timer
    while timer>0:
        print(timer)
        timer-=1
        time.sleep(1)

def write():
    global timer
    while timer>0:
        p.typewrite('Welcome to BB Coder Guy and press the subscribe button for more cool stuffs like this')

def main():
    thr1 = th.Thread(target=start_timer)
    thr1.start()
    thr2 = th.Thread(target=write)
    thr2.start()

main()
