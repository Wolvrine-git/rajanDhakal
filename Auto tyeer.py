import pyautogui , time
a = pyautogui
time.sleep(4)
for i in range(10000):
    a.write("enter text here")
    a.press("enter")