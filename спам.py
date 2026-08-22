import pyautogui as spam
import time
while True:
    try:
        количевсто_спама=int(input("количевство спама:"))
    except ValueError:
        print("только цифры")
        continue

    текст_длл_спама=str(input("текст для спама:"))
    break

i=0
print("у вас есть 3 секунды")
time.sleep(3)

while i<количевсто_спама:
    spam.typewrite(текст_длл_спама)
    spam.press('Enter')
    i += 1